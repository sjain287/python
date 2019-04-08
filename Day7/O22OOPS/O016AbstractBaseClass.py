from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self):
        print("Acc Ctor")

    @abstractmethod
    def withdraw(self):
        pass


class SA(Account):
    pass


class Current(Account):
    def withdraw(self):
        print("Curr_job")


curr = Current()
curr.withdraw()

acc = Account()
acc.withdraw()

saving = SA()
saving.withdraw()
