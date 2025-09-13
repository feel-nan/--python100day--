import json

my_dict = {
    'name': '佐助',
    'age': 18,
    'friends': ['漩涡鸣人', '春野樱'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}

# print(json.dumps(my_dict))
with open('data.json', 'w') as file:
    json.dump(my_dict, file)  # 将字典写入到文件中