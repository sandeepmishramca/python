class Customer():
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def withdrow(self,amount):
        if amount>self.balance:
            raise RuntimeError('Amount is greater than avialable balance')
        self.balance-=amount
        return self.balance

    def deposit(self,amount):
        self.balance+=amount
        return self.balance

    def display(self):
        print("Name ",self.name,"Balance: ",self.balance)

instance=Customer('Mohan',1000.0)
instance.deposit(1200)
instance.display()
instance.withdrow(100.90)
instance.display()
att1=getattr(instance,'balance')
print('The attribute name :',att1)
#delattr(instance,'name')
instance.display()
instance.display()
instance.display()
