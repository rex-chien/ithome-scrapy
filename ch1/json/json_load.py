import json

with open('mock_data.json', newline='') as jsonfile:
    data = json.load(jsonfile)
    # data = json.loads(jsonfile.read())
    print(data)
