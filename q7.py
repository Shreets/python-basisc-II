# 7. Create a list of tuples of first name, last name, and age for your friends and colleagues.
# If you don't know the age, put in None. Calculate the average age, skipping over any None values. ' \
# 'Print out each name, followed by old or young if they are above or below the average age.

bio_list = [('shreeti', 'upreti', 24), ('saru', 'shrestha', None), ('jasmin', 'tiwari', 19), ('stuti', 'upreti', 36)]
age_sum=0
total_items=0


for items in bio_list:
    total_items=total_items+1
    if items[2] is not None:
        age_sum = age_sum + items[2]

average_age = age_sum/total_items

for items in bio_list:
    if items[2] is None:
        print(f'{items[0]} {items[1]}\'s age is unknown')
    elif items[2] >= average_age:
        print(f'{items[0]} {items[1]} is {items[2]} year old, i.e above average age')
    else :
        print(f'{items[0]} {items[1]} is {items[2]} year old, i.e below average age')

#OUTPUT
# shreeti upreti is 24 year old, i.e above average age
# saru shrestha's age is unknown
# jasmin tiwari is 19 year old, i.e below average age
# stuti upreti is 36 year old, i.e above average age



