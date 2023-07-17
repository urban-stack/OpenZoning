import json
from jsonschema import validate, ValidationError

schema_data = {
    "municipality": ["../schema_municipality.json", "../data/municipality.json"],
}

# Unit Tests

# Municipality

# Load the schema file
with open(schema_data["municipality"][0], 'r') as file:
    schema = json.load(file)


###
with open(schema_data["municipality"][1], 'r') as file:

    data = json.load(file)

# Validate the data
try:
    validate(instance=data, schema=schema)
    print('Data is valid')
except ValidationError as e:
    print('Data is not valid:', e)
