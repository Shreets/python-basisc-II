# 4. Create a list. Append the names of your colleagues and friends to it. Has the id of the list changed?
# Sort the list. What is the first item on the list? What is the second item on the list?

friends_list = {'Peter', 'Louis', 'Stewie', 'Brian', 'Meg', 'Chris'}
new_list=[]
for names in friends_list:
    new_list.append(names)

print(f'The unsorted new list is : {new_list}')
new_list.sort()
print(f'the sorted list of frineds is : {new_list}')

# # OUTPUT
# The unsorted new list is : ['Peter', 'Louis', 'Stewie', 'Brian', 'Meg', 'Chris']
## In unsorted list the order of the list remains the same as initial list. The first item is Peter and second is Louis

# the sorted list of friends is : ['Brian', 'Chris', 'Louis', 'Meg', 'Peter', 'Stewie']
## In sorted list the orders are arranges in alphabetic order. First item is Brian and second Chris
