# 13. Write a function to write a comma-separated value (CSV) file. It should accept a filename and
# a list of tuples as parameters. The tuples should have a name, address, and age.
# The file should create a header row followed by a row for each tuple. If the following list of tuples was passed in:
# [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)] it should write the following in the file:
# name,address,age George,4312 Abbey Road,22 John,54 Love Ave,21
import csv

tup = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]

with open('q13_tuple_csv.txt', mode='w') as tuple_file:
    writer = csv.writer(tuple_file)
    writer.writerow(['name', 'address', 'age'])
    for items in tup:
        writer.writerow(items)

# OUTPUT
#
# name,address,age
#
# George,4312 Abbey Road,22
#
# John,54 Love Ave,21

