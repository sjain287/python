class Bank:
    def Withdraw(anyname):  # we can use any parameter,but the general convention is 'self'
        print("Withdraw done")


bnk = Bank()
bnk.Withdraw()

print(type(bnk))

print(bnk.__class__)

print(isinstance(bnk, Bank))
print(isinstance(bnk, object))
print(isinstance(bnk, int))
