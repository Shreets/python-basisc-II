# 8. Write a function, is_prime, that takes an integer and returns True if
# the number is prime and False if the number is not prime.


num = int(input('enter a number to check if it is prime : '))


def is_prime(number):
    count = 0
    if number == 1:
        return True
    elif number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                count = count+1

    if count >= 1:
        return False
    else:
        return True


print(f'Is the number Prime ? {is_prime(num)}')

# OUTPUT
# enter a number to check if it is prime : 3
# Is the number Prime ? True