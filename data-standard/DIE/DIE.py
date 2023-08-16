

import re
import os
import json
import argparse
import geopandas as gpd
from datetime import datetime
from shapely.geometry import Polygon


# This script can be run from the command line. It accepts a short code representing the base directory (i.e. `minn` where the districts subdirectory resides), as well as either a series of coordinates or a GIS file to represent a parcel.
# It will find any districts that intersect with the parcel and write the results to a JSON file output/intersecting_districts_{timestamp}.json.

# You can run the script with coordinates like this:
# python scripts/return_intersecting_districts.py minn --coords x1 y1 x2 y2 x3 y3

# Or with a GIS file like this:
# python scripts/return_intersecting_districts.py minn --file path_to_your_file


# TODO: Make this file able to process multiple parcels, right now it takes in cordinates and outputs what it currently outputs


import re
import os
import json
import argparse
import geopandas as gpd
from datetime import datetime
from shapely.geometry import Polygon
import sys
import pandas as pd
import numpy as np


def find_intersecting_districts(parcel, district_folder):

   ########### This can be extracted to avoid repeated work ###################

    # List all geojson files in the directory that start with a number and underscore
    files = [f for f in os.listdir(district_folder) if f.endswith(
        '.geojson') and re.match(r'^\d+_', f)]

    # Sort files based on priority
    files = sorted(files, key=lambda x: int(x.split('_')[0]))

    #########################################################################

    # Initialize an empty list to store our data
    intersections = []

    for file in files:
        # Extract the priority number from the filename
        priority = int(file.split('_')[0])
        file_name = re.sub(r'(\d+_)(.*)(\.geojson)', r'\2', file)

        # Load the geojson file into a geopandas GeoDataFrame
        gdf = gpd.read_file(os.path.join(district_folder, file))

        # Check for intersection with the parcel
        intersection = gdf[gdf.geometry.intersects(parcel.iloc[0])]

        # Calculate the area of the intersection
        # Project to World Cylindrical Equal Area CRS
        intersection = intersection.to_crs(epsg=4087)

        # Now calculate the area
        intersection_area = intersection.area
        gdf_area = gdf["Shape__Area"]

        # Calculate the percentage overlap
        overlap_percentage_gdf = ((intersection_area / gdf_area) * 100).sum()

        # For each intersecting district, append priority, file name, and district to our data list
        for index, row in intersection.iterrows():
            intersections.append(
                (priority, file_name, row['ZONE_CODE'], overlap_percentage_gdf))

    # Sort according to ascending priority and descending overlap
    intersections.sort(key=lambda x: (x[0], -x[3]))
    print('intersections: ', intersections)

    data = [intersections[0]]

    # Iterate over the rest of the elements
    for tup in intersections[1:]:
        # If the priority is the same as the last element in the result
        if tup[0] == data[-1][0]:
            # Skip this element (it has a lower overlap_percentage_gdf)
            continue
        # Otherwise, add this element to the result
        data.append(tup)

    return data


def main(short_code, coords=None, file=None):
    # Check if parcel is given as coordinates or as a GIS file
    if coords:
        if len(coords) % 2 != 0 or len(coords) < 6:
            raise ValueError(
                "Coordinates should be given as pairs and there should be a minimum of 3 pairs.")
        parcel_coords = list(zip(coords[::2], coords[1::2]))
        parcel = gpd.GeoSeries(Polygon(parcel_coords))
    elif file:
        gdf = gpd.read_file(file)
        gdf["district_all"] = None

        # district_folder = os.path.join('.', short_code, 'districts')

        district_folder = "/app/data-standard/DIE/minn/district"

        for index, row in gdf.iterrows():
            print(gdf['PID'].iloc[index])
            # parcel = gpd.GeoSeries(row.geometry.values[0])

            parcel = gpd.GeoSeries(row.geometry)

            data = find_intersecting_districts(parcel, district_folder)

            # Convert the list of tuples to a list of dictionaries for better JSON compatibility
            data = [{"priority": item[0], "file_name": item[1], "district": item[2]}
                    for item in data]

            gdf.at[index, "district_all"] = data

    else:
        raise ValueError(
            "Either coordinates or a GIS file should be provided for the parcel.")

    # # Get the current timestamp to append to the filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # # Define the output filename and path
    output_filename = f'intersecting_districts_{timestamp}.json'
    output_path = os.path.join('output', output_filename)

    # # Create the output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # # Write the resulting list of dictionaries to a JSON file
    with open(output_path, 'w') as outfile:
        json.dump(data, outfile)

    print(gdf["district_all"][0])


if __name__ == "__main__":
    # NOTE: This is only for testing purposes and instead of the file path being hard coded, it should be taken as an input
    # from the pipeline before it

    # Also add this file to the test folder in DIE for this to work
    # I was unable to find this file
    main("minn", file="/app/data-standard/DIE/test/LHE_4_parcels_BFI3.gpkg")
