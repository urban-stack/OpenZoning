
import os
import tempfile
import processing


# Get the path of the parcels layer
#parcels_path = os.path.join(os.path.dirname(__file__), './processing/Minn_parcels_sample.geojson')
parcels_path = os.path.join(QgsProject.instance().homePath(), 'processing/Minn_parcels_sample.geojson')
#print(parcels_path)

# Get the path of the streets layer
#streets_path = os.path.join(os.path.dirname(__file__), './processing/Minn_streets_sample.geojson')
streets_path = os.path.join(QgsProject.instance().homePath(), 'processing/Minn_streets_sample.geojson')

# Explode the parcels layer
exploded_parcels_path = processing.run("native:explodelines", {
    'INPUT': parcels_path,
    'OUTPUT': 'memory:'
})['OUTPUT']

# Create a buffer around the streets layer
streets_buffer_path = processing.run("native:buffer", {
    'INPUT': streets_path,
    'DISTANCE': 0.001,
    'SEGMENTS': 5,
    'END_CAP_STYLE': 0,
    'JOIN_STYLE': 0,
    'MITER_LIMIT': 2,
    'DISSOLVE': False,
    'OUTPUT': 'memory:'
})['OUTPUT']

# Intersect the exploded parcels layer with the buffer
intersected_parcels_path = processing.run("native:intersection", {
    'INPUT': exploded_parcels_path,
    'OVERLAY': streets_buffer_path,
    'OUTPUT': 'memory:'
})['OUTPUT']

# Create a temporary output file
temp_output = tempfile.gettempdir()
temp_output_path = os.path.join(temp_output, 'output.shp')

# Save the intersected parcels layer to the temporary output file
processing.run("qgis:saveselectedfeatures", {
    'INPUT': intersected_parcels_path,
    'OUTPUT': temp_output
})

# Load the temporary output file
temp_output_layer = QgsVectorLayer(temp_output_path, 'temp_output', 'ogr')

# Create a categorization expression
expression = 'CASE WHEN $id IN (SELECT $id FROM "{}" WHERE "{}" IS NOT NULL) THEN "FRONT" ELSE "REAR" END'.format(
    temp_output_layer.name(),
    temp_output_layer.fields()[0].name()
)

# Categorize the exploded parcels layer
processing.run("qgis:fieldcalculator", {
    'INPUT': exploded_parcels_path,
    'FIELD_NAME': 'category',
    'FIELD_TYPE': 0,
    'FIELD_LENGTH': 10,
    'FIELD_PRECISION': 3,
    'NEW_FIELD': True,
    'FORMULA': expression,
    'OUTPUT': 'memory:'
})

# Print the results
print('Processing complete!')