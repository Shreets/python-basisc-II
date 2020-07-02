# 14. Write a function that reads a CSV file. It should return a list of dictionaries, using the first row as key names,
# and each subsequent row as values for those keys. For the data in the previous example it would return:
# [{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name': 'John', 'address': '54 Love Ave', 'age': 21}]

import csv

# with open('csv_text.txt', mode='w') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow((['Name', 'Address', 'Age']))
#     writer.writerow((['Shreeti', 'Kathmandu', '24']))
#     writer.writerow((['Saru', 'Lalitpur', '25']))
#     writer.writerow((['Jasmin', 'Bhaktapur', '23']))

with open('csv_text.txt', mode='r') as csv_file:
    reader = csv.DictReader(csv_file)
    dict_list = []
    for item in reader:
        print(item)
        dict_list.append(item)


print(dict_list)

# OUTPUT
#
# {'Name': 'Shreeti', 'Address': 'Kathmandu', 'Age': '24'}
# {'Name': 'Saru', 'Address': 'Lalitpur', 'Age': '25'}
# {'Name': 'Jasmin', 'Address': 'Bhaktapur', 'Age': '23'}

# [{'Name': 'Shreeti', 'Address': 'Kathmandu', 'Age': '24'}, {'Name': 'Saru', 'Address': 'Lalitpur', 'Age': '25'}, {'Name': 'Jasmin', 'Address': 'Bhaktapur', 'Age': '23'}]

