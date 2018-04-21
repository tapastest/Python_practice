import yaml

# Reading YAML data

file_name = 'D:\Project\@Python\YAML_DataProvider.yml'
with open(file_name, 'r') as f:
    data = yaml.load(f)
    # Example 1
print(data["VesselTypes"][0]["Draughts"][0]["Name"])
    # Example 2
print(data["Vessels"][0]["Name"])
    # Example 3
print(data["Vessels"][1]["Name"])       # Max 1 can as 1 column