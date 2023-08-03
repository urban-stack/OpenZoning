import json as json

# Add base_data, and change this accordingly on how to handle it asking Luke


def extract_nested_constraints(nested_dict, base_data=None):
    constraints = {}
    for k, v in nested_dict.items():
        #
        # print(f"Key : {k},\n v:{v} \n\n")
        if k == "bulkOptionality":
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

        elif k == "constraintsModule":
            continue

        elif k == "setbacks":
            print(f"k: {k} \n")
            print(f"v: {v} \n \n")
            extracted_constraints = extract_nested_constraints(
                v, base_data)

            for k, v in extracted_constraints.items():
                # Add a new dictionary with the key "setbacks", and assign the original value to it
                constraints[k] = {"setbacks": v}

        elif isinstance(v, dict):
            # print("\n\n")
            # print("!!!!!! DICT GOING DOWN A LEVEL !!!!!!!")
            # print(f"Key : {k},\n v:{v} \n\n")

            extracted_constraints = extract_nested_constraints(v, base_data)
            constraints = {
                k: {**constraints.get(k, {}), **v} for k, v in extracted_constraints.items()}

            # print("***** DICT GOING UP A LEVEL *****!")
            # print("constraints: ")
            # print(constraints)
        elif isinstance(v, list):
            for i, item in enumerate(v):
                # print(f"Key: {k}")

                # print("ITEMS IN LIST: ", item)
                if isinstance(item, dict):
                    # print("\n")
                    # print("!!!!!! DICT1 GOING DOWN A LEVEL !!!!!!!")
                    # print(f"Key : {k},\n v:{v} \n\n")
                    extracted_constraints = extract_nested_constraints(
                        item, base_data)
                    constraints = {
                        k: {**constraints.get(k, {}), **v} for k, v in extracted_constraints.items()}

                    # constraints.update(
                    #     extract_nested_constraints(item, base_data))
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
        open('../schema_vikranth/tests/data/districts/R2B_multipleFamily_district.json', 'r'))

    constraints = {}
    for i, constraint in enumerate(data['constraints']):
        # constraints[f"constraint_{i+1}"] = extract_nested_constraints(
        #     constraint,  base_data)

        temp_constraint = extract_nested_constraints(
            constraint,  base_data)

        # print(temp_constraint)
        # print("\n\n")

        for key, value in temp_constraint.items():
            if key in constraints:
                constraints[key].update(value)
            else:
                constraints[key] = value

    # print({data['district']['districtType']: constraints})

    return {data['district']['districtType']: constraints}


# extract_nested_constraints_wrapper(
#     '../schema_vikranth/tests/data/districts/BFI3_district.json')
