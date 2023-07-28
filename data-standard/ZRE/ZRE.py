from nested_constraints_extractor import extract_nested_constraints_wrapper


def merge_dictionaries_based_on_hierarchy(dicts, hierarchy):
    """
    Function to merge dictionaries based on a hierarchy.
    In case of duplicate keys, the value from the dictionary with the higher hierarchy is used.

    Since the format of the constraints returned is:

    {

    overlay_2: {
    Height:{}
    },
    overlay_1: {
    FAR:{}
    },
    base: {
    FAR:{}
    },
    superDistrict: {
    FAR:{}
    }

    we can start from superDistrict and go down the hierarchy, updating if there are similar keys.

    }
    """
    merged_dict = {}

    # final_list = []

    for hierarchy_level in hierarchy:
        for key, value in dicts.items():
            if key == hierarchy_level:
                if key not in merged_dict:
                    merged_dict[key] = value
                else:
                    merged_dict[key].update(value)

    return merged_dict


# Define the hierarchy
districtsHierarchy = ["superDistrict", "base", "overlay_1", "overlay_2"]

# Test extractions
"../"


# Make this more automated basically running the files in a for loop

file1 = extract_nested_constraints_wrapper(
    '../schema_vikranth/tests/data/districts/BFI3_district.json')
file2 = extract_nested_constraints_wrapper(
    '../schema_vikranth/tests/data/districts/super_district.json')
# file3 = extract_nested_constraints_wrapper(
#     '../schema_vikranth/tests/data/districts/overall.json')
print("-----------------------------------")
# print(file1)
print("-----------------------------------")
# print(file2)
print("-------------****************---------------")


merged_dict = {**file1, **file2}


# Merge the dictionaries based on the hierarchy
merge_output = merge_dictionaries_based_on_hierarchy(
    merged_dict, districtsHierarchy)

aggregate_data = {}

for key in merge_output:

    for sub_key in merge_output[key]:

        if sub_key in aggregate_data:
            aggregate_data[sub_key].update(merge_output[key][sub_key])

        else:
            aggregate_data[sub_key] = merge_output[key][sub_key]

ZRE_output = {
    "final_constraints": aggregate_data,
    **merge_output
}

print("-------------********THISSSSS********---------------")
print(ZRE_output)
