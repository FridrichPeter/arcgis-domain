import arcpy
import arcgis
from arcgis.gis import GIS
from arcgis.features import FeatureLayer
import csv

# Path to your CSV file containing domain values
csv_path = 'your_path_here.csv'
with open(csv_path) as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header
    coded_values = [{'name': row[0], 'code': int(row[1])} for row in reader]

# Setup your GIS connection
gis = GIS("your_gis_url_here","your_username","your_password")

# Example: updating a single geodatabase item
item_id = "your_item_id_here"
item = gis.content.get(item_id)

# Update each feature layer in the item
for i in range(number_of_layers):
    feature_layer = FeatureLayer(item.url + "/" + str(i))
    feature_layer.manager.update_definition({
        'fields': [{'name': 'your_field_name',
                    'domain': {'type': 'codedValue', 'name': 'your_field_name', 'codedValues': coded_values}}]
    })

print("Update complete!")
