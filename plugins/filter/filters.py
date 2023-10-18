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


class FilterModule(object):
    """Ansible core jinja2 filters"""

    def filters(self):
        return {
            "extractor": extractor,
            "deep_merge_dicts": deep_merge_dicts,
            "bool_converter": bool_converter,
        }
