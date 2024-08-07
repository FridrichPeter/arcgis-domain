import arcpy
import arcgis
from arcgis.gis import GIS
from arcgis.features import FeatureLayer
import csv
import time

#Path to your domain CSV
csv_path = r"path_to_your_domain_csv.csv"
with open(csv_path) as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    coded_values = [{'name': row[0], 'code': int(row[1])} for row in reader]
print(coded_values[-1])

# Connect to the GIS
gis = GIS("your_gis_url", "your_username", "your_password")

# Get item URL for the modeling gdb
item_id_modeling = "item_id_for_modeling_gdb"
item = gis.content.get(item_id_modeling)

for i in range(6):  # range = number of layers
    feature_layer_url = item.url + "/" + str(i)
    feature_layer = FeatureLayer(feature_layer_url)
    service_url = feature_layer.url

    url = service_url
    field_name = 'field_name_for_model_id'

    fl = arcgis.features.FeatureLayer(url, gis)
    fl.manager.update_definition({
        'fields': [{'name': field_name, 'domain': {'type': 'codedValue', 'name': field_name, 'codedValues': coded_values}}]
    })

    print(f"Layer {i} modeling done")

item_id_mpo = "item_id_for_mpo_gdb"
item = gis.content.get(item_id_mpo)

for i in range(6):  # range = number of layers
    feature_layer_url = item.url + "/" + str(i)
    feature_layer = FeatureLayer(feature_layer_url)
    service_url = feature_layer.url

    url = service_url
    field_name = 'field_name_for_kod_hdm'

    fl = arcgis.features.FeatureLayer(url, gis)
    fl.manager.update_definition({
        'fields': [{'name': field_name, 'domain': {'type': 'codedValue', 'name': field_name, 'codedValues': coded_values}}]
    })

    print(f"Layer {i} MPO done")
