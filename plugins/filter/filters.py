# flake8: noqa E501
from ansible.errors import AnsibleError
import yaml
import json

def extractor(data, defaults, path):
    """
    Traverse the data based on the given path and return scalar values along \
          the path.

    Args:
    - data (dict): The data to traverse.
    - path (str): Path to traverse.

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
    paths = path.split('/')
    outter_results = extract_values(data, paths, "")
    defaults = extract_values(defaults, paths, "")
    final_result = []
    for entry in outter_results:
        if defaults:
            for default_key, default_value in defaults[0].items():
                if default_key not in entry:
                    entry[default_key] = default_value
        final_result.append(entry)
    return final_result


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


def list_assembler(item, options, names):
    results = []
    for index, data in enumerate(names):
        if data in item:
            if item[data]:
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


def static_ports_assembler(data):
    result = []
    grouped_data = {}
    prefix = "apic_tenants_application_profiles_endpoint_groups_static_ports"

    for entry in data:        
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


def list_of_dict_diff(list1, list2):
    set1 = {json.dumps(d, sort_keys=True) for d in list1}
    set2 = {json.dumps(d, sort_keys=True) for d in list2}
    
    diff = set2 - set1

    return [json.loads(s) for s in diff]


def present_extracted_data_assembler(previous_dict, current_dict):
    results = {}
    for key, value in current_dict.items():
        if key in previous_dict:
            dict_diff = list_of_dict_diff(previous_dict[key], current_dict[key])
            if dict_diff:
                results[key]= dict_diff
        else:
            results[key] = value
    return results


def absent_extracted_data_assembler(previous_dict, current_dict):
    results = {}
    for key, value in previous_dict.items():
        if key in current_dict:
            dict_diff = list_of_dict_diff(current_dict[key],previous_dict[key])
            if dict_diff:
                results[key]= dict_diff
        else:
            results[key] = value
    return results


class FilterModule(object):
    """Ansible core jinja2 filters"""

    def filters(self):
        return {
            "extractor": extractor,
            "deep_merge_dicts": deep_merge_dicts,
            "bool_converter": bool_converter,
            "list_assembler": list_assembler,
            "ip_cidr_extractor": ip_cidr_extractor,
            "static_ports_assembler": static_ports_assembler,
            "present_extracted_data_assembler": present_extracted_data_assembler,
            "absent_extracted_data_assembler": absent_extracted_data_assembler
        }
