class Bank:  # class naming convention used- Pascal casing
    def __init__(self, accId, amount, name):
        self.accId = accId
        self.amount = amount
        self.name = name
        print(f"Account opened for {self.name}")

    def Withdraw(self, amount):  # self- reference of invoking object
        self.amount -= amount
        print(f"Withdraw done {self.name}")

    def getBalance(self):
        return f"Balance in Acc# {self.accId} is {self.amount}, Mr.{self.name}"


sachin = Bank(101, 40000, "Sachin")
saurav = Bank(102, 50000, "Saurav")
print
print(sachin.getBalance())
print(saurav.getBalance())

sachin.Withdraw(10000)
saurav.Withdraw(5000)

print(sachin.getBalance())
print(saurav.getBalance())
