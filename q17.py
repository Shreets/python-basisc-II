# 17. Write a program that serves as a basic calculator. It asks for two numbers, then it asks for an operator.
# Gracefully deal with input that doesn't cleanly convert to numbers. Deal with division by zero errors.

first_num = int(input('Enter first number : '))
second_num = int(input('Enter second number : '))
operator = input('Enter operator : ')


def calculator(num1, num2, op):
    if op == '+':
        return num1 + num2
    if op == '-':
        return num1 - num2
    if op == '*':
        return num1 * num2
    try:
        if op == '/':
            return num1 / num2
    except ZeroDivisionError:
        print('The number cannot be divided by 0. Please try again with another number')


calculate = calculator(first_num, second_num, operator)
print(calculate)
