# 11. Create a variable, filename. Assuming that it has a three-letter extension, and using slice operations,
# find the extension. For README.txt, the extension should be txt. Write code using slice operations that will give the
# name without the extension. Does your code work on filenames of arbitrary length?

input_file = input('Enter filename : ')
filename_list = list(input_file)
new_list = []
for i in input_file:
    if i != '.':
        new_list.append(i)
    else:
        break

filename = ''.join(new_list)

print(f'The filename without it\'s extension is : {filename}')

#OUTPUT

# Enter filename : README.txt
# The filename without it's extension

# Enter filename : python_first_assignment.py
# The filename without it's extension is : python_first_assignment
