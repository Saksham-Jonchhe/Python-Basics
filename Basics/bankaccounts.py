class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,initialAmount,acctName):
        self.balance=initialAmount
        self.name=acctName
        print(f"\n Account '{self.name}' created. \nBalance=${self.balance:.2f}")

    def getbalance(self):
        print(f"\n Account '{self.name}' balance= ${self.balance:.2f}")

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("\nDeposit Complete.")
        self.getbalance()

    def viableTransaction(self,amount):
        if self.balance>=amount:
            return 
        else:
            raise BalanceException(
                f"\nSorry,account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance=self.balance-amount
            print("\nWithdraw Complete")
            self.getbalance()
        except BalanceException as error:
            print(f"\WIthdraw interrupted: {error}")


    def transfer(self,amount,account):
        try:
            print("\n*******\n\nBeginning Transfer...🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\n Transfer Complete ✅")
        except BalanceException as error:
            print(f"\n Transfer interrupted . {error}")

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance=self.balance+(amount*1.05)
        print("\nDeposit complete")
        self.getbalance()

class savingsAccount(InterestRewardsAcct):
    def __init__(self,initialAmount,acctName):
        super().__init__(initialAmount,acctName)
        self.fee=5
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance -(amount + self.fee)
            print("\nWIthdraw completed.")
            self.getbalance()
        except BalanceException as error:
            print(f"\nWithdraw Interrupted:{error}")
