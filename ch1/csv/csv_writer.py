import csv
with open('mock_data.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([3, 'Corri', 'Campling', 'Female', 'Sweden'])

with open('mock_data.csv', 'a', newline='') as csvfile:
    fieldnames = ['id', 'first_name', 'last_name', 'gender', 'country']
    writer = csv.DictWriter(csvfile, fieldnames, delimiter=',', quotechar='"')
    writer.writerow({
        'id': 4,
        'first_name': 'Salvatore',
        'last_name': 'Gaitskill',
        'gender': 'Male',
        'country': 'Indonesia'
    })
