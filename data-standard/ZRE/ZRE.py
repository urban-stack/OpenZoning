from nested_constraints_extractor import extract_nested_constraints_wrapper
import os
import geopandas as gpd


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


def post_processing_final_constraints(merge_output, lots_gpkg):

    agrregate_data = {}

    ZRE_output_list = []

    # Define the required districtTypeGroups
    available_districtTypes = {"Residential": "R",
                               "Office Residential": "OR"}

    # Add final_constraints column

    for key in merge_output:

        for sub_key in merge_output[key]:

            if sub_key in agrregate_data:
                agrregate_data[sub_key].update(merge_output[key][sub_key])

            else:
                agrregate_data[sub_key] = merge_output[key][sub_key]

    # Run a python loop here that goes through each row in the gpkg file and extracts the zoning and PID columns
    # and sends it to post_processing_final_constraints function which then changes the final_constraints
    # to a list of JSON arrays

    for index, row in lots_gpkg.iterrows():

        temp_output = {
            "final_constraints": agrregate_data,
            **merge_output
        }

        # For testing
        row["ZONING"] = "R3"

        zoning = row["ZONING"][0]
        PID = row["PID"]

        # extract only the required districtTypeGroups by taking input from GeoPackage file

        for bulkType, constraints in temp_output["final_constraints"].items():

            if "districtTypeGroups" not in constraints:
                continue

            districtTypeGroups = constraints["districtTypeGroups"]

            # for districtType, value in districtTypeGroups.items():
            # print("-------------********sssssss********---------------\n\n")
            # print(districtType in available_districtTypes)
            # print(zoning)
            # print(zoning == available_districtTypes[districtType])
            # print("-------------********sssssss********---------------\n\n")

            # if(districtType in available_districtTypes and zoning == available_districtTypes[districtType]):
            #     bulkType[available_districtTypes[districtType]
            #              ] = value[available_districtTypes[districtType]]
            #     break
            # print("-------------********THISSSSS********---------------\n\n")
            # print(constraints)
            # print("-------------****************---------------\n\n")

            # del constraints["districtTypeGroups"]

        # if(index == 0):
        #     print(temp_output)

        ZRE_output_list.append({"PID": PID, "constraints": temp_output})

    return ZRE_output_list


# Define the hierarchy
districtsHierarchy = ["superDistrict", "base", "overlay_1", "overlay_2"]

# Read the geopackage file and extract the needed information

# Load the geojson file into a geopandas GeoDataFrame which has all the parcels
gdf = gpd.read_file(
    "../schema_vikranth/tests/data/geopkgs/lowry_hill_east_first_five.gpkg")

# print(gdf.columns.tolist)


# Make this more automated basically running the files in a for loop

file1 = extract_nested_constraints_wrapper(
    '../schema_vikranth/tests/data/districts/BFI3_district.json')

# file2 = extract_nested_constraints_wrapper(
# '../schema_vikranth/tests/data/districts/BFI3_district.json')
file2 = extract_nested_constraints_wrapper(
    '../schema_vikranth/tests/data/districts/super_district.json')


# file3 = extract_nested_constraints_wrapper(
#     '../schema_vikranth/tests/data/districts/overall.json')


merged_dict = {**file1, **file2}


# Merge the dictionaries based on the hierarchy
merge_output = merge_dictionaries_based_on_hierarchy(
    merged_dict, districtsHierarchy)


# Post processing of the final constraints

ZRE_output = post_processing_final_constraints(merge_output, gdf)


print("-------------********THISSSSS********---------------\n\n")
print(ZRE_output)
print("\n\n----------------------------\n\n")
