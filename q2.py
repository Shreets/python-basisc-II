# 2. Write an if statement to determine whether a variable holding a year
# is a leap year.

year = input('enter a year to check if it is a leap year : ')

if int(year) % 4 == 0 and int(year) % 100 != 0:
    print(f'The year {year} is a leap year')
else:
    print(f'The year {year} is NOT a leap year')

# OUTPUT

# enter a year to check if it is a leap year : 2000
# The year 2000 is NOT a leap year

# enter a year to check if it is a leap year : 2012
# The year 2012 is a leap year
