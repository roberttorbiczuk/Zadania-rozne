class BankAccount:

    _next_acc_number = 1

    @classmethod
    def get_next_acc_number(cls):
        next = cls._next_acc_number
        cls._next_acc_number += 1
        return next

    def __init__(self, ):
        self._number = self.get_next_acc_number()  # sprawdz jak zrobisz bez nawiasow
        self._cash = 0.0


    # def __init__(self, ):
    #     #  self.__class__ - klasa naszego obiektu
    #     self._number = self._next_acc_number
    #     self.__class__._next_acc_number += 1
    #     self._cash = 0.0

    def get_cash(self):
        return self._cash

    def get_number(self):
        return self._number

    def deposit_cash(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            self._cash += amount
        else:
            print("Warning: incorrect deposit amount: %s" % amount)

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount < 0:
            print("Cannot withdraw amount: {}.".format(amount))
            return
        if amount <= self._cash:
            self._cash -= amount
            return amount
        else:
            amount_withdrawed = self._cash
            self._cash = 0
            return amount_withdrawed


account = BankAccount()
print("lol")
print(account.withdraw(100000))
print(account.get_cash())
print(account.deposit_cash(100234))
print(account.withdraw("dwa"))
print(account.get_cash())
print(account.get_number())

print(account._number)
acc2 = BankAccount()
print(acc2._number)
acc3 = BankAccount()

print(acc3._number)




