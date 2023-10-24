# flake8: noqa E501
from typing import List, Dict, Any, Union, Optional
from ansible.errors import AnsibleError
from ansible.utils.display import Display
import json

def extractor(data: Dict[str, Any], defaults: Dict[str, Any], path: str) -> List[Dict[str, Any]]:
    """
    Traverse the data based on the given path and return scalar values along the path.
    
    Args:
    - data (Dict[str, Any]): The data to traverse.
    - defaults (Dict[str, Any]): Default values to be merged if certain keys are missing.
    - path (str): Path to traverse.
    
    Returns:
    - List[Dict[str, Any]]: A list of dictionaries containing scalar values along the path.
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
                data[current_path], rest_path, prefix + current_path + "/"
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
                        item[current_path], rest_path, prefix + current_path + "/"
                    )
                    for deeper_dict in deeper_values:
                        combined_dict = {**scalars, **deeper_dict}
                        results.append(combined_dict)
            return results

        # If path not found, return empty
        return []

    if not isinstance(data, dict) or not isinstance(path, str):
        raise AnsibleError("Invalid input data or path provided to extractor.")

    # Begin extraction from the top-level data
    paths = path.split('/')
    
    if not paths:
        raise AnsibleError(f"Invalid path provided: {path}.")
    
    try:
        outter_results = extract_values(data, paths, "")
    except Exception as e:
        raise AnsibleError(f"Error in extractor filter while extract data from {path}: {str(e)}")
    
    if not isinstance(defaults, dict):
        raise AnsibleError("Invalid defaults provided to extractor.")
    try:
        defaults = extract_values(defaults, paths, "")
    except Exception as e:
        raise AnsibleError(f"Error in extractor filter while extract defaults from {path}: {str(e)}")
    
    try:
        final_result = []
        for entry in outter_results:
            if defaults:
                for default_key, default_value in defaults[0].items():
                    if default_key not in entry:
                        entry[default_key] = default_value
            final_result.append(entry)
    except Exception as e:
        raise AnsibleError(f"Error in extractor filter while merge data and defaults: {str(e)}")
    
    return final_result


def deep_merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """
    Recursively merges dict2 into dict1.
    
    Args:
    - dict1 (Dict[str, Any]): The primary dictionary that will be merged into.
    - dict2 (Dict[str, Any]): The dictionary that will be merged from.
    
    Returns:
    - Dict[str, Any]: The merged dictionary.
    
    Raises:
    - AnsibleError: If either of the input is not a dictionary or any other error occurs.
    """
    
    
    try:
        if not isinstance(dict1, dict):
            Display().warning("First deep_merge_dicts argument is not a dict. Return only data in second arguments.")
            if not isinstance(dict2, dict):
                raise AnsibleError("Both inputs to deep_merge_dicts is not dictionaries. At least one of two input is dictionary.")
            return dict2
        if not isinstance(dict2, dict):
            Display().warning("Second deep_merge_dicts argument is not a dict. Return only data in first arguments.")
            return dict1
    
        for key, value in dict2.items():
            if key in dict1:
                if isinstance(dict1[key], dict) and isinstance(value, dict):
                    deep_merge_dicts(dict1[key], value)
                elif isinstance(dict1[key], list) and isinstance(value, list):
                    dict1[key].extend(value)
                else:
                    dict1[key] = value
            else:
                dict1[key] = value

        return dict1

    except Exception as e:
        raise AnsibleError(f"Error in deep_merge_dicts filter: {str(e)}")


def bool_converter(value: Union[bool, Any]) -> str:
    """
    Convert boolean true/false to 'enabled'/'disabled'.
    
    Args:
    - value (Union[bool, Any]): The value to convert. Expected to be a boolean, 
                                but other types are returned as-is.
    
    Returns:
    - str: 'enabled' if value is True, 'disabled' if value is False, 
           otherwise returns the value itself.
    
    Raises:
    - AnsibleError: If there's an error during the conversion process.
    """
    
    try:
        if isinstance(value, bool):
            return "enabled" if value else "disabled"
        return value

    except Exception as e:
        raise AnsibleError(f"Error in bool_converter filter: {str(e)}")


def list_assembler(item: Dict[str, Any], options: List[str], names: List[str]) -> List[str]:
    """
    Assemble a list based on the presence of keys in the input item.

    Args:
    - item (Dict[str, Any]): The dictionary containing key-value pairs.
    - options (List[str]): A list of strings representing possible options.
    - names (List[str]): A list of keys that we need to check in the item.

    Returns:
    - List[str]: A list containing selected options based on the presence of names in the item.
    
    Raises:
    - AnsibleError: If there's an error during the list assembly process.
    """
    
    try:
        results = []
        for index, data in enumerate(names):
            if data in item and item[data]:
                results.append(options[index])
        return results

    except Exception as e:
        raise AnsibleError(f"Error in list_assembler filter: {str(e)}")


def ip_cidr_extractor(data: str, part: str) -> Optional[str]:
    """
    Extract IP address or CIDR from a given IP/CIDR string.

    Args:
    - data (str): The IP/CIDR string.
    - part (str): The part to extract, either 'ip' or 'cidr'.

    Returns:
    - Optional[str]: Extracted IP or CIDR part. Returns None if the part isn't found.
    
    Raises:
    - AnsibleError: If there's an error during the extraction or if an invalid 'part' argument is provided.
    """
    
    try:
        ip_address, _, cidr = data.partition('/')
        
        if part == "ip":
            return ip_address
        elif part == "cidr":
            return cidr
        else:
            raise ValueError("The 'part' argument must be either 'ip' or 'cidr'.")

    except Exception as e:
        raise AnsibleError(f"Error in ip_cidr_extractor filter: {str(e)}")


def static_ports_assembler(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Assemble static port configurations based on the provided data.

    Args:
    - data (List[Dict[str, Any]]): The list of dictionaries containing static port configurations.

    Returns:
    - List[Dict[str, Any]]: A list of dictionaries with assembled static port configurations.
    
    Raises:
    - AnsibleError: If there's an error during the assembly process.
    """
    def get_key(entry):
        return (
            entry['apic/tenants/name'], 
            entry['apic/tenants/application_profiles/name'], 
            entry['apic/tenants/application_profiles/endpoint_groups/name']
        )

    try:
        grouped_data = {}
        prefix = "apic/tenants/application_profiles/endpoint_groups/static_ports/"

        for entry in data:        
            key = get_key(entry)

            grouped_data.setdefault(key, {
                "tenant": entry['apic/tenants/name'],
                "ap": entry['apic/tenants/application_profiles/name'],
                "epg": entry['apic/tenants/application_profiles/endpoint_groups/name'],
                "interface_configs": []
            })

            leafs = [entry[f'{prefix}node_id']]
            if f'{prefix}node2_id' in entry:
                leafs.append(entry[f'{prefix}node2_id'])
            
            pod_id = entry[f'{prefix}pod_id']
            extpaths = []
            interface = entry.get(f'{prefix}channel', f'{entry[prefix + "module"]}/{entry[prefix + "port"]}')

            if f'{prefix}node_id' in entry and f'{prefix}channel' not in entry:
                
                if f'{prefix}sub_port' in entry:
                    interface += f'/{entry[prefix + "sub_port"]}'
                    interface_type = 'switch_port'
                elif f'{prefix}/fex_id' in entry:
                    extpaths = [str(entry[f'{prefix}/fex_id'])]
                    interface_type = 'fex'
                else:
                    interface_type = 'switch_port'
            else:
                interface_type = 'vpc' if f'{prefix}/node2_id' in entry else 'port_channel'

            interface_config = {
                "encap_id": entry[f'{prefix}vlan'],
                "interface": interface,
                "leafs": leafs,
                "pod_id": pod_id,
                "interface_mode": entry[f'{prefix}mode'],
                "deploy_immediacy": entry[f'{prefix}deployment_immediacy'],
                "interface_type" : interface_type,
            }

            if extpaths:
                interface_config["extpaths"] = extpaths
            if f'{prefix}description' in entry:
                interface_config["description"] = entry[f'{prefix}description'] 

            grouped_data[key]['interface_configs'].append(interface_config)

        return list(grouped_data.values())

    except Exception as e:
        raise AnsibleError(f"Error in static_ports_assembler filter: {str(e)}")


def list_of_dict_diff(list1: list, list2: list) -> list:
    """
    Determine the difference between two lists of dictionaries.
    
    Args:
        list1 (list): The first list of dictionaries.
        list2 (list): The second list of dictionaries.
        
    Returns:
        list: A list of dictionaries that are in list2 but not in list1.
        
    Raises:
        AnsibleError: If an error occurs during the process.
    """
    try:
        set1 = {json.dumps(d, sort_keys=True) for d in list1}
        set2 = {json.dumps(d, sort_keys=True) for d in list2}
        
        diff = set2 - set1
        return [json.loads(s) for s in diff]
    except Exception as e:
        raise AnsibleError(f"Error in 'list_of_dict_diff' func: {str(e)}")


def present_extracted_data_assembler(previous_dict: dict, current_dict: dict) -> dict:
    """
    Assemble the present extracted data by determining the difference between
    the current dictionary and the previous dictionary.
    
    Args:
        previous_dict (dict): The previous dictionary.
        current_dict (dict): The current dictionary.
        
    Returns:
        dict: A dictionary with keys from the current dictionary where the values
              are different from those in the previous dictionary.
        
    Raises:
        AnsibleError: If an error occurs during the process.
    """
    try:
        results = {}
        for key, value in current_dict.items():
            # If the key exists in both dictionaries, find the difference
            if key in previous_dict:
                dict_diff = list_of_dict_diff(previous_dict[key], current_dict[key])
                if dict_diff:
                    results[key] = dict_diff
            # If the key only exists in the current dictionary, add it to the results
            else:
                results[key] = value
        return results
    except Exception as e:
        raise AnsibleError(f"Error in 'present_extracted_data_assembler' filter: {str(e)}")


def absent_extracted_data_assembler(previous_dict: dict, current_dict: dict) -> dict:
    """
    Assemble the absent extracted data by determining the difference between
    the previous dictionary and the current dictionary.
    
    Args:
        previous_dict (dict): The previous dictionary.
        current_dict (dict): The current dictionary.
        
    Returns:
        dict: A dictionary with keys from the previous dictionary where the values
              are different from those in the current dictionary.
        
    Raises:
        AnsibleError: If an error occurs during the process.
    """
    try:
        results = {}
        for key, value in previous_dict.items():
            # If the key exists in both dictionaries, find the difference
            if key in current_dict:
                dict_diff = list_of_dict_diff(current_dict[key], previous_dict[key])
                if dict_diff:
                    results[key] = dict_diff
            # If the key only exists in the previous dictionary, add it to the results
            else:
                results[key] = value
        return results
    except Exception as e:
        raise AnsibleError(f"Error in 'absent_extracted_data_assembler' filter: {str(e)}")


def find_value(extracted_data: dict, path: str, identified_key: str, identified_value: str, key_to_find: str) -> str:
    """
    Search within the extracted data to find a specific value based on the provided path, identified key, and value.
    
    Args:
        extracted_data (dict): The data to search within.
        path (str): The path indicating where to look within the data.
        identified_key (str): The key to identify the desired data.
        identified_value (str): The value to identify the desired data.
        key_to_find (str): The key whose value needs to be found.
        
    Returns:
        str: The value associated with the key_to_find if found, otherwise None.
        
    Raises:
        AnsibleError: If an error occurs during the search process.
    """
    try:
        # Check if the path exists in the extracted_data
        if path in extracted_data:
            for item in extracted_data[path]:
                # Match based on the identified_key and identified_value
                if identified_key in item and item[identified_key] == identified_value:
                    return item.get(key_to_find)
        return None
    except Exception as e:
        raise AnsibleError(f"Error in 'find_value' filter: {str(e)}")


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
            "absent_extracted_data_assembler": absent_extracted_data_assembler,
            "find_value": find_value
        }
