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
            print(v)
            for option in v:
                # Check if "bulks" is a list or a string and convert to list if necessary
                bulks = option["bulks"] if isinstance(
                    option["bulks"], list) else [option["bulks"]]

                print("this is bulks")

                print(bulks)

                print("\n")

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

                           # Issue
                           ## Status : Pending
                            #  This is the issue because the
                            # old districtTypeGroups is being replaced
                            #  by the new one

                            # What you need to do here is take in the old value
                            # make sure its added to the new one and also add the new
                            # value to it

                            # Especially when there nare two districtTypeGroups objects
                            # this is the issue

                            # constraints[k] = {
                            #     "districtTypeGroups": {
                            #         districtType: v for districtType in districtTypes
                            #     }
                            # }
            return constraints
            #################################
            #     for district in districtTypes:
            #         if district not in constraints:
            #             constraints[district] = {}

            #         # print(len(option.items()))

            #         for key, value in option.items():
            #             # print(key)
            #             if key != "districtTypes":
            #                 # print(value)

            #                 extracted_constraints = extract_nested_constraints(
            #                     {key: value}, base_data)

            #                 constraints[district] = extracted_constraints
            # return {"districtTypeGroups": constraints}

        elif k == "constraintsModule":
            continue

        elif k == "setbacks":
            # print(f"k: {k} \n")
            # print(f"v: {v} \n \n")
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
            # print("\n\n")
            # print("!!!!!! DICT GOING DOWN A LEVEL !!!!!!!")
            # print(f"Key : {k},\n v:{v} \n\n")

            extracted_constraints = extract_nested_constraints(v, base_data)
            print(constraints)
            print(k)
            for k1, v1 in extracted_constraints.items():
                prevBulkConstaints = constraints.get(k1, {})
                tempConstraints = {k: v1}
                constraints[k1] = {**prevBulkConstaints, **tempConstraints}

            # constraints = {
            #     #  k: {**constraints.get(k1, {}), **v1} for k1, v1 in extracted_constraints.items()}

            #     # This works for most cases
            #     k: {**constraints.get(k, {}), **v} for k, v in extracted_constraints.items()}

            print(constraints)

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
                    # for k1, v1 in extracted_constraints.items():
                    #     prevBulkConstaints = constraints.get(k1, {})
                    #     tempConstraints = {k: v1}
                    #     constraints[k1] = {
                    #         **prevBulkConstaints, **tempConstraints}

                    # constraints.update(
                    #     extract_nested_constraints(item, base_data))

                # What happens if its not a dict???

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
    # constraints = []

    for i, constraint in enumerate(data['constraints']):
        # constraints[f"constraint_{i+1}"] = extract_nested_constraints(
        #     constraint,  base_data)

        temp_constraint = extract_nested_constraints(
            constraint,  base_data)

        # print(temp_constraint)
        # print("\n\n")

        constraints = merge_dicts(constraints, temp_constraint)

        # for key, value in temp_constraint.items():
        # if key in constraints:
        #     constraints[key].update(value)
        # else:
        #     constraints[key] = value

        # constraints[key] = {**constraints.get(key, {}), **value}

    # print({data['district']['districtType']: constraints})

    return {data['district']['districtType']: constraints}


# Comment this once the function is tested
# final_constraints = extract_nested_constraints_wrapper(
#     '../schema_vikranth/tests/data/districts/BFI3_district.json')

# print("Nested constraitns\n")
# print(final_constraints)
