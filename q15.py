# 15. Imagine you are designing a banking application. What would a customer look like? What attributes would she have?
# What methods would she have?


class Customer:

    def __init__(self, first_name, last_name, deposit, withdrawal, currency):
        self.first_name = first_name
        self.last_name = last_name
        self.deposit = deposit
        self.withdrawal = withdrawal
        self.currency = currency

    def transaction(self):
        print(
            f'Hello {self.first_name}! Your total Transaction this month is {self.currency}.{self.deposit - self.withdrawal}')


customer1 = Customer('Shreeti', 'Upreti', 100000, 8965, 'Rs')
customer1.transaction()

customer2 = Customer('Jason', 'Mamoa', 8395701, 324518, '$')
customer2.transaction()

# output
#
# Hello Shreeti! Your total Transaction this month is Rs.91035
# Hello Jason! Your total Transaction this month is $.8071183
