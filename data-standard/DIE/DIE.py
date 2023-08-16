

import re
import os
import json
import argparse
import geopandas as gpd
from datetime import datetime
from shapely.geometry import Polygon


def find_intersecting_districts(parcel, district_folder):
    # List all geojson files in the directory that start with a number and underscore
    files = [f for f in os.listdir(district_folder) if f.endswith(
        '.geojson') and re.match(r'^\d+_', f)]

    # Initialize an empty list to store our data
    data = []

    # Sort files based on priority
    files = sorted(files, key=lambda x: int(x.split('_')[0]))

    for file in files:
        # Extract the priority number from the filename
        priority = int(file.split('_')[0])
        file_name = re.sub(r'(\d+_)(.*)(\.geojson)', r'\2', file)

        # Load the geojson file into a geopandas GeoDataFrame
        gdf = gpd.read_file(os.path.join(district_folder, file))

        # Check for intersection with the parcel
        intersection = gdf[gdf.geometry.intersects(parcel.iloc[0])]
        print("gdf: ")
        print(gdf)

        # For each intersecting district, append priority, file name, and district to our data list
        for index, row in intersection.iterrows():

            data.append((priority, file_name, row['ZONE_CODE']))

    return data


def main():

    # Change this filepath to the location of the geopackage file or make it as an argument

    # Change the below PATH!!

    gdf = gpd.read_file(
        "/app/data-standard/DIE/test/minn_parcels_alldistricts_corner_sample.gpkg")

    # Extract the geometry to create a GeoSeries
    parcel = gpd.GeoSeries(gdf.geometry.values[0])

    district_folder = "/app/geo-standard/minn/district"

    data = find_intersecting_districts(parcel, district_folder)

    # Convert the list of tuples to a list of dictionaries for better JSON compatibility
    data = [{"priority": item[0], "file_name": item[1], "district": item[2]}
            for item in data]

    # Get the current timestamp to append to the filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Define the output filename and path
    output_filename = f'intersecting_districts_{timestamp}.json'
    output_path = os.path.join('output', output_filename)

    # Create the output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Write the resulting list of dictionaries to a JSON file
    with open(output_path, 'w') as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    main()
