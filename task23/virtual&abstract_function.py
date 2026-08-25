# implement virtual function and abstract function for any real time requirement



from abc import ABC, abstractmethod

class BankAccount(ABC):
    
    def withdraw(self,amount):
        print("withdraw amount:",amount)

    @abstractmethod
    def cal_interest(self):
        pass

class savingsAccount(BankAccount):
    
    def cal_interest(self):
        print("Interest rate: 3%")

account=savingsAccount()
account.withdraw(5000)
account.cal_interest()
