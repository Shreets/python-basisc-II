# 10. Write a function that takes camel-cased strings (i.e. ThisIsCamelCased), and converts them to snake case
# (i.e. this_is_camel_cased).
# Modify the function by adding an argument, separator, so it will also convert to the kebab case (i.e.this-is-camel-case) as well.

input_string = input('Enter a camel case string you want to convert : ')
index = []


def replace_camel(string, separator):
    for i in string[1:]:
        if i.isupper():
            index.append(i)
            string = string.replace(i, separator + i)
    return string[1:].lower()


kebab_case = replace_camel(input_string, '-')
snake_case = replace_camel(input_string, '_')
print(index)
print(f'The string in kebab case is as follows : \n {kebab_case}\n ')
print(f'The string in snake case is as follows : \n {snake_case}\n ')

# OUTPUT
#
# Enter a camel case string you want to convert: ThisIsSolutionForNumberTenQuestionOfPythonAssignment

# The string in kebab case is as follows:
#  this-is-solution-for-number-ten-question-of-python-assignment

# The string in snake case is as follows:
#  this_is_solution_for_number_ten_question_of_python_assignment
