from bankaccounts import *

Saksham=BankAccount(1000,"Saksham")
Sara=BankAccount(1000,"Sara")

Saksham.getbalance()
Sara.getbalance()
Sara.deposit(500)

Saksham.withdraw(10000)
Saksham.withdraw(10)

Saksham.transfer(10000,Sara)
Saksham.transfer(100,Sara)

jim=InterestRewardsAcct(1000,"Jim")
jim.getbalance()
jim.deposit(100)
jim.transfer(100,Saksham)

blaze=savingsAccount(1000,'Blaze')
blaze.getbalance()
blaze.deposit(100)
blaze.transfer(10000,Sara)
