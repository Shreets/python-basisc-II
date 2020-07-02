# 6. Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

friends_list = ['Rachel', 'Joey', 'Chandler', 'Monica', 'Ross', 'Phoebe', 'John']

for friend in friends_list:
    if friend == 'John':
        print(f'You have a friend named John')
        break
else:
    print('No friend name John found')

#OUTPUT

# You have a friend named John
