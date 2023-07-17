import json
from jsonschema import validate, ValidationError

schema_data = {
    "superDistrict": ["../../schema_district.json", "../data/superDistrict.json"],
}

# Unit Tests

# Super District

# Load the schema file
with open(schema_data["superDistrict"][0], 'r') as file:
    schema = json.load(file)


###
with open(schema_data["superDistrict"][1], 'r') as file:

    data = json.load(file)

# Validate the data
try:
    validate(instance=data, schema=schema)
    print('Data is valid')
except ValidationError as e:
    print('Data is not valid:', e)
