from nested_constraints_extractor import extract_nested_constraints_wrapper


def merge_dictionaries_based_on_hierarchy(dicts, hierarchy):
    """
    Function to merge dictionaries based on a hierarchy. 
    In case of duplicate keys, the value from the dictionary with the higher hierarchy is used.
    """
    merged_dict = {}
    for d in dicts:
        for key, value in d.items():
            if key.split('-')[0] in hierarchy:
                if key in merged_dict:
                    # If the key is already in the merged_dict, only update the value if the current hierarchy is higher
                    if hierarchy.index(key.split('-')[0]) > hierarchy.index(merged_dict[key].split('-')[0]):
                        merged_dict[key] = value
                else:
                    merged_dict[key] = value
    return merged_dict


# Define the hierarchy
districtsHierarchy = ["superDistrict", "base", "overlay_1", "overlay_2"]

# Test extractions

file1 = extract_nested_constraints_wrapper(
    '../schema_vikranth/tests/data/districts/BFI3_district.json')
file2 = extract_nested_constraints_wrapper(
    '../schema_vikranth/tests/data/districts/super_district.json')
# file3 = extract_nested_constraints_wrapper(
#     '../schema_vikranth/tests/data/districts/overall.json')

print(extract_nested_constraints_wrapper)
print(file1)


# Merge the dictionaries based on the hierarchy
merged_dict_hierarchy = merge_dictionaries_based_on_hierarchy(
    [file1, file2], districtsHierarchy)
merged_dict_hierarchy
