dict1 = {'apple': 2, 'banana': 3, 'cherry': 5}
dict2 = {'banana': 4, 'cherry': 2, 'date': 7}

merged_dict = {}

for key in dict1.keys() | dict2.keys():
    if (v1 := dict1.get(key)) is not None and (v2 := dict2.get(key)) is not None:
        merged_dict[key] = v1 + v2
    else:
        merged_dict[key] = v1 if (v1 := dict1.get(key)) is not None else dict2.get(key)

print("Merged dictionary:", merged_dict)
