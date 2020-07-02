# 5. Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the corresponding information
# from your friends and append them to the list. Sort the list. When you learn about sort method,
# you can use the key parameter to sort by any field in the tuple, first name, last name, or age.

bio1_tuple = ('shreeti','upreti',24)
bio2_tuple = ('saru','shrestha',14)
bio3_tuple = ('jasmin','tiwari',19)
bio4_tuple = ('stuti','upreti',36)

people = []


def list_of_people(*args):
    for arg in args:
        people.append(arg)
    return people

people_list = list_of_people(bio1_tuple, bio2_tuple, bio3_tuple, bio4_tuple)

people_list.sort(key= lambda item:item[2])

print(f'list of bio tuples sorted by age are: {people_list}')

#OUTPUT

# list of bio tuples sorted by age are: [('saru', 'shrestha', 14), ('jasmin', 'tiwari', 19), ('shreeti', 'upreti', 24), ('stuti', 'upreti', 36)]





