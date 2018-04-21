import json

with open('D:\Project\@Python\JSON_DataProvider.json', 'r') as file:
    json_dict = json.load(file)


print (json_dict["office"]["medical"][4]["room-number"])

