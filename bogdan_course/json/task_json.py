import json


my_dict = {
    "bike": 'Ducati',
    "color": 'red',
    "vol": 1.2,
    "like": True,
    "gear": [1, 2, 3, 4, 5, 6]
}

json_from_dict = json.dumps(my_dict, indent=1)
print(json_from_dict)
print(type(json_from_dict))
