import json as json

# Add base_data, and change this accordingly on how to handle it asking Luke


def merge_dicts(d1, d2):
    merged = {}
    for key in set(d1.keys()) | set(d2.keys()):
        if key in d1 and key in d2:
            if isinstance(d1[key], dict) and isinstance(d2[key], dict):
                merged[key] = merge_dicts(d1[key], d2[key])
            else:
                merged[key] = d1[key] if d1[key] == d2[key] else (
                    d1[key], d2[key])

        elif key in d1:
            merged[key] = d1[key]
        else:
            merged[key] = d2[key]
    return merged


def extract_nested_constraints(nested_dict, base_data=None):
    constraints = {}
    for k, v in nested_dict.items():
        #
        # print(f"Key : {k},\n v:{v} \n\n")
        if k == "bulkOptionality":
            # print(v)
            for option in v:
                # Check if "bulks" is a list or a string and convert to list if necessary
                bulks = option["bulks"] if isinstance(
                    option["bulks"], list) else [option["bulks"]]

                for bulk in bulks:
                    if bulk not in constraints:
                        constraints[bulk] = {}
                    for key, value in option.items():
                        if key != "bulks":
                            constraints[bulk][key] = value

        elif k == "districtTypeGroups":

            for option in v:

                # add all districtTypes to contraints

                districtTypes = option["districtTypes"] if isinstance(
                    option["districtTypes"], list) else [option["districtTypes"]]

                for key, value in option.items():

                    if key != "districtTypes":
                        extracted_constraints = extract_nested_constraints(
                            {key: value}, base_data)

                        for k, v in extracted_constraints.items():
                            if k not in constraints:
                                constraints[k] = {"districtTypeGroups": {}}
                                constraints[k] = {
                                    "districtTypeGroups": {
                                        districtType: v for districtType in districtTypes
                                    }
                                }
                            else:
                                constraints[k]["districtTypeGroups"].update(
                                    {districtType: v for districtType in districtTypes})

            return constraints

        elif k == "constraintsModule":
            continue

        elif k == "setbacks":

            extracted_constraints = extract_nested_constraints(
                v, base_data)

            for k, v in extracted_constraints.items():
                # Add a new dictionary with the key "setbacks", and assign the original value to it
                constraints[k] = {"setbacks": v}

        elif k == "lotCoverage":
            extracted_constraints = extract_nested_constraints(
                v, base_data)

            for k, v in extracted_constraints.items():
                # Add a new dictionary with the key "setbacks", and assign the original value to it
                constraints[k] = {"lotCoverage": v}

        elif k == "lot":
            extracted_constraints = extract_nested_constraints(
                v, base_data)

            return extracted_constraints

        elif isinstance(v, dict):

            extracted_constraints = extract_nested_constraints(v, base_data)

            for k1, v1 in extracted_constraints.items():
                prevBulkConstaints = constraints.get(k1, {})
                tempConstraints = {k: v1}
                constraints[k1] = {**prevBulkConstaints, **tempConstraints}

        elif isinstance(v, list):
            for i, item in enumerate(v):
                # print(f"Key: {k}")

                # print("ITEMS IN LIST: ", item
                if isinstance(item, dict):

                    extracted_constraints = extract_nested_constraints(
                        item, base_data)
                    constraints = {
                        k: {**constraints.get(k, {}), **v} for k, v in extracted_constraints.items()}

        else:
            # Check if 'bulkOptionality' was not encountered and base_data is available
            if not any("bulkOptionality" in bulk for bulk in constraints) and base_data:
                for bulk in base_data["usePermissions"]["permitted"]:

                    # constraints[bulk] = { k: v}
                    constraints[bulk] = {**constraints[bulk],
                                         k: v} if bulk in constraints else {k: v}

        # print("constraints: ", constraints)

    return constraints


def extract_nested_constraints_wrapper(file_path):
    # Extract all nested constraints
    data = json.load(
        open(file_path, 'r'))

    base_data = json.load(
        open('/app/data-standard/schema_vikranth/tests/data/districts/R2B_multipleFamily_district.json', 'r'))

    constraints = {}
    # constraints = [

    for i, constraint in enumerate(data['constraints']):

        temp_constraint = extract_nested_constraints(
            constraint,  base_data)

        constraints = merge_dicts(constraints, temp_constraint)

    return {data['district']['districtType']: constraints}


# Comment this once the function is tested
# final_constraints = extract_nested_constraints_wrapper(
#     '/app/data-standard/schema_vikranth/tests/data/districts/BFI3_district.json')

# print("Nested constraitns\n")
# print(final_constraints)
