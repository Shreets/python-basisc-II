# 12. Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.


input_string = input('Enter a string : ')

def is_palindrome(string):
    string_list = list(string)
    list_reverse = reversed(string_list)
    reverse_string = ''.join(list_reverse)
    if reverse_string == string:
        print(f'The string {string} is palindrome')
    else:
        print(f'The string {string} is not palindrome')


is_palindrome(input_string)

#OUTPUT
# Enter a string : deed
# The string deed is palindrome