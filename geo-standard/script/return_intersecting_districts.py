##This script can be run from the command line. It accepts a short code representing the base directory (i.e. `minn` where the districts subdirectory resides), as well as either a series of coordinates or a GIS file to represent a parcel. 
##It will find any districts that intersect with the parcel and write the results to a JSON file output/intersecting_districts_{timestamp}.json.

# You can run the script with coordinates like this:
## python scripts/return_intersecting_districts.py minn --coords x1 y1 x2 y2 x3 y3

# Or with a GIS file like this:
## python scripts/return_intersecting_districts.py minn --file path_to_your_file



import re
import os
import json
import argparse
import geopandas as gpd
from datetime import datetime
from shapely.geometry import Polygon

def find_intersecting_districts(parcel, district_folder):
    # List all geojson files in the directory that start with a number and underscore
    files = [f for f in os.listdir(district_folder) if f.endswith('.geojson') and re.match(r'^\d+_', f)]

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

        # For each intersecting district, append priority, file name, and district to our data list
        for index, row in intersection.iterrows():
            data.append((priority, file_name, row['ZONE_CODE']))

    return data

def main():
    parser = argparse.ArgumentParser(description='Find intersecting districts for a given parcel.')
    parser.add_argument('short_code', help='Short code representing the base directory.')
    parser.add_argument('--coords', nargs='+', type=float, help='Coordinates of the parcel. Should be in the format --coords x1 y1 x2 y2 x3 y3 ...')
    parser.add_argument('--file', type=str, help='GIS file representing the parcel.')

    args = parser.parse_args()

    # Check if parcel is given as coordinates or as a GIS file
    if args.coords:
        if len(args.coords) % 2 != 0 or len(args.coords) < 6:
            raise argparse.ArgumentTypeError("Coordinates should be given as pairs and there should be a minimum of 3 pairs.")
        parcel_coords = list(zip(args.coords[::2], args.coords[1::2]))
        parcel = gpd.GeoSeries(Polygon(parcel_coords))
    elif args.file:
        gdf = gpd.read_file(args.file)
        parcel = gpd.GeoSeries(gdf.geometry.values[0])  # Extract the geometry to create a GeoSeries
    else:
        raise argparse.ArgumentTypeError("Either coordinates or a GIS file should be provided for the parcel.")


    district_folder = os.path.join('.', args.short_code, 'districts')

    data = find_intersecting_districts(parcel, district_folder)

    # Convert the list of tuples to a list of dictionaries for better JSON compatibility
    data = [{"priority": item[0], "file_name": item[1], "district": item[2]} for item in data]
    
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
