
# hybrid

class cal():
    
    def __init__(self, x=100,y=50):

        self.a =x
        self.b =y

class addition(cal):
    def add(self):
        self.c= self.a+self.b
        print(" Addition : ",self.c)

class subtraction(cal):
    def sub(self):
        self.c= self.a-self.b
        print(" Subtraction : ",self.c)

class multiple(addition):
    def mul(self):
        self.c= self.a*self.b
        print(" Multiple : ",self.c)

    
        
c1= multiple(20,10)
c1.add()
c1.mul()