import Temp_YAML

class Account:

    def __init__(self, Ac_name=''):
        self.name = Ac_name
        
    def Account_details(self):
        return self.name

New_obj = Account("tapas")
print(New_obj.Account_details())

    # Import function file Temp_YAML.py
Data = Temp_YAML.yml_data()
print(Data["VesselTypes"][0]["Draughts"][0]["Mass"])
    # Example 2
print(Data["Vessels"][0]["Name"])
    # Example 3
print(Data["Vessels"][1]["Name"])