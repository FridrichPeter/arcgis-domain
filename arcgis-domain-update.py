import arcpy
import arcgis
from arcgis.gis import GIS
from arcgis.features import FeatureLayer
import csv

# Path to your CSV file containing domain values
csv_path = 'path/to/your/csv.csv'
with open(csv_path) as csvfile:
    reader = csv.reader(csvfile)
    next(reader) 
    coded_values = [{'name': row[0], 'code': int(row[1])} for row in reader]

# Setup your GIS connection
gis = GIS("your_gis_url_here","your_username","your_password")

# Updating a single geodatabase item
item_id = "your_item_id_here" #https://community.esri.com/t5/arcgis-online-blog/where-can-i-find-the-item-id-for-an-arcgis-online/ba-p/890284
item = gis.content.get(item_id)

# Update each feature layer in the item
for i in range(number_of_layers):
    feature_layer = FeatureLayer(item.url + "/" + str(i))
    feature_layer.manager.update_definition({
        'fields': [{'name': 'your_field_name',
                    'domain': {'type': 'codedValue', 'name': 'your_field_name', 'codedValues': coded_values}}]
    })

print("Update complete, grab a cold beer!")
