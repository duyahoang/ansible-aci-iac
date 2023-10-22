# flake8: noqa E501
from ansible.errors import AnsibleError
import yaml
import json

def extractor(data, *paths):
    """
    Traverse the data based on the given path and return scalar values along \
          the path.

    Args:
    - data (dict): The data to traverse.
    - paths (tuple): Path to traverse.

    Returns:
    - List[Dict]: A list of dictionaries containing scalar values along \
          the path.
    """

    def extract_values(data, paths, prefix):
        results = []

        # Base case: if no more paths, return data
        if not paths:
            if isinstance(data, list):
                for item in data:
                    if not isinstance(item, (dict, list)):
                        results.append({prefix[:-1]: data})
                for item in data:
                    if not isinstance(item, dict):
                        break
                    scalar_values = {
                        prefix + k: v
                        for k, v in item.items()
                        if not isinstance(v, (dict, list))
                    }
                    if scalar_values:
                        results.append(scalar_values)
            elif isinstance(data, dict):
                scalar_values = {
                    prefix + k: v
                    for k, v in data.items()
                    if not isinstance(v, (dict, list))
                }
                if scalar_values:
                    results.append(scalar_values)
            return results

        # Extract current path and rest of the path
        current_path, *rest_path = paths

        # If data is a dictionary and contains current_path
        if isinstance(data, dict) and current_path in data:
            return extract_values(
                data[current_path], rest_path, prefix + current_path + "_"
            )

        # If data is a list of dictionaries
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict) and current_path in item:
                    scalars = {
                        prefix + k: v
                        for k, v in item.items()
                        if not isinstance(v, (dict, list))
                    }
                    deeper_values = extract_values(
                        item[current_path], rest_path, prefix + current_path + "_"
                    )
                    for deeper_dict in deeper_values:
                        combined_dict = {**scalars, **deeper_dict}
                        results.append(combined_dict)
            return results

        # If path not found, return empty
        return []

    # Begin extraction from the top-level data
    return extract_values(data, paths, "")


def deep_merge_dicts(dict1, dict2):
    """
    Recursively merges dict2 into dict1.
    """
    for key, value in dict2.items():
        if key in dict1:
            # If both are dictionaries, merge them
            if isinstance(dict1[key], dict) and isinstance(value, dict):
                deep_merge_dicts(dict1[key], value)
            # If both are lists, concatenate them
            elif isinstance(dict1[key], list) and isinstance(value, list):
                dict1[key].extend(value)
            else:
                dict1[key] = value
        else:
            dict1[key] = value
    return dict1


def bool_converter(boolean):
    """
    Convert boolean true/false to enabled/disabled.
    """
    if isinstance(boolean, bool):
        if boolean is True:
            return "enabled"
        return "disabled"
    return boolean


def value_getter(value_name, item, defaults_dict, *paths):
    value = item.get(value_name, None)
    # If value is None or doesn't exist, fetch the default
    if value is not None:
        return value
    
    results = extractor(defaults_dict, *paths)
    if not results or value_name not in results[0]:
        return None

    return results[0][value_name]


def list_assembler(item, options, names, defaults_dict, *paths):
    results = []
    defaults = extractor(defaults_dict, *paths)
    for index, data in enumerate(names):
        if data in item:
            if item[data]:
                results.append(options[index])
        elif results and data in defaults[0] and defaults[0][data]:
            results.append(options[index])
    return results

def ip_cidr_extractor(data, part):
    ip_address, _, cidr = data.partition('/')
    
    if part == "ip":
        return ip_address
    elif part == "cidr":
        return cidr
    else:
        raise ValueError("The 'part' argument must be either 'ip' or 'cidr'.")


def static_ports_assembler(data, defaults_dict, *paths):
    result = []
    grouped_data = {}
    prefix = "apic_tenants_application_profiles_endpoint_groups_static_ports"
    defaults = extractor(defaults_dict, *paths)

    for entry in data:
        if defaults:
            for default_key, default_value in defaults[0].items():
                if default_key not in entry:
                    entry[default_key] = default_value
        
        key = (entry['apic_tenants_name'], entry['apic_tenants_application_profiles_name'], entry['apic_tenants_application_profiles_endpoint_groups_name'])
        if key not in grouped_data:
            grouped_data[key] = {
                "tenant": entry['apic_tenants_name'],
                "ap": entry['apic_tenants_application_profiles_name'],
                "epg": entry['apic_tenants_application_profiles_endpoint_groups_name'],
                "interface_configs": []
            }

        if f'{prefix}_node2_id' in entry:
            leafs = [entry[f'{prefix}_node_id'], entry[f'{prefix}_node2_id']]
        else:
            leafs = entry[f'{prefix}_node_id']

        extpaths = []
        if f'{prefix}_node_id' in entry and f'{prefix}_channel' not in entry:
            pod_id = entry[f'{prefix}_pod_id']
            if f'{prefix}_sub_port' in entry:
                interface = f'{entry[prefix + "_module"]}/{entry[prefix + "_port"]}/{entry[prefix + "_sub_port"]}'
                interface_type = 'switch_port'
            elif f'{prefix}_fex_id' in entry:
                extpaths = [str(entry[f'{prefix}_fex_id'])]
                interface = f'{entry[prefix + "_module"]}/{entry[prefix + "_port"]}'
                interface_type = 'fex'
            else:
                interface = f'{entry[prefix + "_module"]}/{entry[prefix + "_port"]}'
                interface_type = 'switch_port'
        else:
            interface = entry[f'{prefix}_channel']
            if f'{prefix}_node2_id' in entry:
                interface_type = 'vpc'
            else:
                interface_type = 'port_channel'

        interface_config = {
            "encap_id": entry[f'{prefix}_vlan'],
            "interface": interface,
            "leafs": leafs,
            "pod_id": pod_id,
            "interface_mode": entry[f'{prefix}_mode'],
            "deploy_immediacy": entry[f'{prefix}_deployment_immediacy'],
            "interface_type" : interface_type,
        }
        if extpaths:
            interface_config["extpaths"] = extpaths
        if f'{prefix}_description' in entry:
            interface_config["description"] = entry[f'{prefix}_description'] 

        grouped_data[key]['interface_configs'].append(interface_config)

    result = list(grouped_data.values())
    return result



# with open('/Users/duyhoan/Documents/GitHub-Cisco/Small Scripts/ansible-aci-iac/vars/host_vars/apic1/apic_configuration.yaml', 'r') as file:
#     content = file.read()
with open('/Users/duyhoan/Documents/GitHub-Cisco/Small Scripts/ansible-aci-iac/roles/present_apic/defaults/defaults.yaml', 'r') as file:
    content2 = file.read()

# config1 = yaml.safe_load(content)
default_data = yaml.safe_load(content2)
default = default_data["defaults"]
data = [{'apic_tenants_name': 'PROD', 'apic_tenants_application_profiles_name': 'PROD', 'apic_tenants_application_profiles_endpoint_groups_name': 'EPG_VLAN100', 'apic_tenants_application_profiles_endpoint_groups_bridge_domain': 'BD_VLAN100', 'apic_tenants_application_profiles_endpoint_groups_static_ports_node_id': 101, 'apic_tenants_application_profiles_endpoint_groups_static_ports_port': 1, 'apic_tenants_application_profiles_endpoint_groups_static_ports_vlan': 100}, {'apic_tenants_name': 'PROD', 'apic_tenants_application_profiles_name': 'PROD', 'apic_tenants_application_profiles_endpoint_groups_name': 'EPG_VLAN100', 'apic_tenants_application_profiles_endpoint_groups_bridge_domain': 'BD_VLAN100', 'apic_tenants_application_profiles_endpoint_groups_static_ports_node_id': 102, 'apic_tenants_application_profiles_endpoint_groups_static_ports_port': 1, 'apic_tenants_application_profiles_endpoint_groups_static_ports_vlan': 100}, {'apic_tenants_name': 'PROD', 'apic_tenants_application_profiles_name': 'PROD', 'apic_tenants_application_profiles_endpoint_groups_name': 'EPG_VLAN101', 'apic_tenants_application_profiles_endpoint_groups_bridge_domain': 'BD_VLAN101', 'apic_tenants_application_profiles_endpoint_groups_static_ports_node_id': 101, 'apic_tenants_application_profiles_endpoint_groups_static_ports_port': 1, 'apic_tenants_application_profiles_endpoint_groups_static_ports_vlan': 101}, {'apic_tenants_name': 'PROD', 'apic_tenants_application_profiles_name': 'PROD', 'apic_tenants_application_profiles_endpoint_groups_name': 'EPG_VLAN101', 'apic_tenants_application_profiles_endpoint_groups_bridge_domain': 'BD_VLAN101', 'apic_tenants_application_profiles_endpoint_groups_static_ports_node_id': 102, 'apic_tenants_application_profiles_endpoint_groups_static_ports_port': 1, 'apic_tenants_application_profiles_endpoint_groups_static_ports_vlan': 101}]
out = static_ports_assembler(data, default, "apic", "tenants", "application_profiles", "endpoint_groups", "static_ports")
print(json.dumps(out, indent=2))

# scope_options = ["public", "private", "shared"]
# scope_names = ["apic_tenants_bridge_domains_subnets_public", "apic_tenants_bridge_domains_subnets_private", "apic_tenants_bridge_domains_subnets_shared"]

# print(list_assembler({"apic_tenants_bridge_domains_subnets_private": False, "apic_tenants_bridge_domains_subnets_public": True, "apic_tenants_bridge_domains_subnets_shared": True}, scope_options, scope_names, default,"apic","tenants","bridge_domains","subnets"))
# print(extractor(config1, "apic", "tenants", "application_profiles", "endpoint_groups", "static_ports"))

class FilterModule(object):
    """Ansible core jinja2 filters"""

    def filters(self):
        return {
            "extractor": extractor,
            "deep_merge_dicts": deep_merge_dicts,
            "bool_converter": bool_converter,
            "value_getter": value_getter,
            "list_assembler": list_assembler,
            "ip_cidr_extractor": ip_cidr_extractor,
            "static_ports_assembler": static_ports_assembler
        }
