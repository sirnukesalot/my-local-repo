class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def depo(self):
        amount=float(input("Enter amount of deposit"))
        self.balance+=amount
        print("Deposited:", amount)
    def withdraw(self):
        amount=float(input("Enter amount of withdraw"))
        if self.balance>=amount:
            self.balance-=amount
            print("Currently Withdrawn:", amount)
        else:
            print("Withdraw declined")
    def display(self):
        print("Available balance")
A=Account()
A.depo()
A.withdraw()
A.display()