"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

## Employment classes (Employment is an interface class)
class Employment:
    def getBasePay(self):
        return 0

    def __str__(self):
        return ""
        
class MonthlySalary(Employment):
    def __init__(self, salary):
        self.salary = salary

    def getBasePay(self):
        return self.salary

    def __str__(self):
        return "monthly salary of "+str(self.getBasePay())
    
class HourlySalary(Employment):
    def __init__(self, hourly_rate, hours):
        self.hourly_rate = hourly_rate
        self.hours = hours

    def getBasePay(self):
        return self.hours * self.hourly_rate

    def __str__(self):
        return "contract of "+str(self.hours)+" hours at "+str(self.hourly_rate)+"/hour"

## Commission classes (Commission is an interface class)
class Commission:
    def getCommission(self):
        return 0

    def __str__(self):
        return ""

class BonusCommission(Commission):
    def __init__(self, bonus):
        self.bonus = bonus

    def getCommission(self):
        return self.bonus

    def __str__(self):
        return " and receives a bonus commission of "+str(self.getCommission())

class ContractCommission(Commission):
    def __init__(self, contract_commission, contracts):
        self.contract_commission = contract_commission
        self.contracts = contracts

    def getCommission(self):
        return self.contract_commission * self.contracts

    def __str__(self):
        return " and receives a commission for "+str(self.contracts)+" contract(s) at "+str(self.contract_commission)+"/contract"

class Employee:
    def __init__(self, name, employment, commission):
        self.name = name
        self.employment = employment
        self.commission = commission

    def get_pay(self):
        return int(self.employment.getBasePay()) + int(self.commission.getCommission())

    def __str__(self):
        temp_string = self.name+" works on a "
        return self.name+" works on a "+str(self.employment)+str(self.commission)+".  Their total pay is "+str(self.get_pay())+"."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', MonthlySalary(4000), Commission())

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlySalary(25, 100), Commission())

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlySalary(3000), ContractCommission(200, 4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlySalary(25, 150), ContractCommission(220, 3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlySalary(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlySalary(30, 120), BonusCommission(600))
