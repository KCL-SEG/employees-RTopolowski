"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, pay, hours, bonus_commission, contract_commission, contracts_number):
        self.name = name
        self.hours = hours
        self.pay = pay
        self.bonus_commission = bonus_commission
        self.contract_commission = contract_commission
        self.contracts_number = contracts_number

    def get_pay(self):
        if self.hours < 0:
            return self.pay + self.bonus_commission + (self.contract_commission * self.contracts_number)
        else:
            return (self.pay * self.hours) + self.bonus_commission + (self.contract_commission * self.contracts_number)

    def __str__(self):
        temp_string = self.name+" works on a "
        if self.hours < 0:
            temp_string += "monthly salary of "+str(self.pay)
        else:
            temp_string += "contract of "+str(self.hours)+" hours at "+str(self.pay)+"/hour"

        if self.bonus_commission > 0:
            temp_string += " and receives a bonus commission of "+str(self.bonus_commission)
        elif self.contract_commission > 0 and self.contracts_number > 0:
            temp_string += " and receives a commission for "+str(self.contracts_number)+" contract(s) at "+str(self.contract_commission)+"/contract"

        temp_string += ".  Their total pay is "+str(self.get_pay())+"."
        return temp_string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, -1, 0, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 25, 100, 0, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, -1, 0, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 25, 150, 0, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, -1, 1500, 0, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 30, 120, 600, 0, 0)
