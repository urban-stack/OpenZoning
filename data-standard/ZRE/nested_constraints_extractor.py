import json as json


def extract_nested_constraints(nested_dict, parent_key=""):

    items = []
    for k, v in nested_dict.items():
        new_key = f"{parent_key}-{k}" if parent_key else k
        if k == "bulks":
            items.append((new_key, v))
        elif isinstance(v, dict):
            items.extend(extract_nested_constraints(v, new_key).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, dict):
                    items.extend(extract_nested_constraints(
                        item, f"{new_key}_{i}").items())
                else:
                    items.append((f"{new_key}_{i}", item))
        else:
            items.append((new_key, v))
    return dict(items)


def extract_nested_constraints_wrapper(file_path):
    # Extract all nested constraints
    data = json.load(
        open(file_path, 'r'))

    print("here")

    constraints = {}
    for i, constraint in enumerate(data['constraints']):
        constraints[f"constraint_{i+1}"] = extract_nested_constraints(
            constraint, data['district']['districtType'])

    # print(constraints)
