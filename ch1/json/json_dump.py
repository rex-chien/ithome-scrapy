import json
with open('mock_data.json', newline='') as jsonfile:
    data = json.load(jsonfile)

with open('mock_data.json', 'w', newline='') as jsonfile:
    data.append({
        'id': 5,
        'first_name': 'Vin',
        'last_name': 'Sturdgess',
        'gender': 'Male',
        'country': 'Greece'
    })
    json.dump(data, jsonfile)
    # jsonfile.write(json.dumps(data))
