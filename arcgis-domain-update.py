from arcgis.gis import GIS
import csv

# Connect to the GIS
gis = GIS("your_gis_url", "your_username", "your_password")

# If your data is feature service
item = gis.content.get("item_id")  # Replace "item_id" with your actual item ID. Could not to find item ID: https://community.esri.com/t5/arcgis-online-blog/where-can-i-find-the-item-id-for-an-arcgis-online/ba-p/890284
domain_fld_name = "fld_name"  # Replace "fld_name" with your actual field name

# Read domain values from a CSV file
csv_path = "path_to_your_domain_csv.csv"  # Your csv path
with open(csv_path) as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  
    coded_values = []
    for row in reader:
        #Checking whether each code is numerical or textual
        try:
            code = int(row[1])  #Try converting to integer
        except ValueError:
            code = row[1]  # Use string if it fails
        coded_values.append({'name': row[0], 'code': code})

# Update each feature layer using the coded values read from the CSV
for fl in item.layers:
    # Check if the field exists in the layer
    field_names = [field['name'] for field in fl.properties.fields]
    if domain_fld_name in field_names:
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
    else:
        print(f"Field '{domain_fld_name}' not found in {fl.properties.name}, skipping update.")

print("Update process completed.") # Thanks Glen!
