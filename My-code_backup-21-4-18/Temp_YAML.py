import yaml


def yml_data():

    # Reading YAML data
    file_name = 'D:\Project\@Python\YAML_DataProvider.yml'
    with open(file_name, 'r') as f:
        data = yaml.load(f)
        return data

if __name__ == "__main__":
    Data = yml_data()
    print(Data["VesselTypes"][0]["Draughts"][0]["Name"])
