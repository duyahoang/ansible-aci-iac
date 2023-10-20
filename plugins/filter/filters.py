# flake8: noqa E501
from ansible.errors import AnsibleError
import yaml

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


class FilterModule(object):
    """Ansible core jinja2 filters"""

    def filters(self):
        return {
            "extractor": extractor,
            "deep_merge_dicts": deep_merge_dicts,
            "bool_converter": bool_converter,
            "value_getter": value_getter,
            "list_assembler": list_assembler,
            "ip_cidr_extractor": ip_cidr_extractor
        }
