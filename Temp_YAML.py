import yaml

# Reading YAML data
file_name = 'D:\Project\@Python\YAML_DataProvider.yml'
with open(file_name, 'r') as f:
    data = yaml.load(f)

print(data["VesselTypes"][0]["Draughts"][0]["Name"])
