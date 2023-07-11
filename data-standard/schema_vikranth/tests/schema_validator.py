import json
from jsonschema import validate, ValidationError

schema_data = {
    "superDistrict": ["../schema_district file.json", "../../examples/Minneapolis/Minneapolis_superDistrict_0.0.9_07212022.json"],
    "municipality": ["../schema_municipality.json", "../../examples/Minneapolis/Minneapolis_municipality_0.1_B_07042023.json"],
}

# Load the schema file
with open(schema_data["superDistrict"][0], 'r') as file:
    schema = json.load(file)

# Your data

# TODO: Create a for loop that loops through the data files in the data folder and validates them against the schema
with open(schema_data["superDistrict"][1], 'r') as file:
    data = json.load(file)

# Validate the data
try:
    validate(instance=data, schema=schema)
    print('Data is valid')
except ValidationError as e:
    print('Data is not valid:', e)
