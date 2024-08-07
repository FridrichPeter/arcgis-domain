from arcgis.gis import GIS
import csv

# Connect to the GIS
gis = GIS("your_gis_url", "your_username", "your_password")

#If your item is a feature service
item = gis.content.get("item_id")  # Replace "item_id" with your actual item ID
domain_fld_name = "fld_name"  # Replace "fld_name" with your actual field name

#Read domain values from a CSV file
csv_path = "path_to_your_domain_csv.csv"  # Path to your csv
with open(csv_path) as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    coded_values = [{'name': row[0], 'code': int(row[1])} for row in reader]

#  Update each feature layer using the coded values read from the CSV
for fl in item.layers:
    fl.manager.update_definition({
        'fields': [{
            'name': domain_fld_name,
            'domain': {
                'type': 'codedValue',
                'name': domain_fld_name,
                'codedValues': coded_values
            }
        }]
    })
    print(f"Domain updated for {fl.properties.name}")

print("All layers have been updated.")
