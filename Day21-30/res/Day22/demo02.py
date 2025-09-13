import json

with open('data.json', 'r') as file:
    my_dict = json.load(file)
    print(my_dict)
    print(type(my_dict))