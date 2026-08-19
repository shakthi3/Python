
class demo():
    
    def __init__(self, x=100,y=50):

        self.a =x
        self.b =y

    def add(self):
        self.c= self.a+self.b
        print(" Addition : ",self.c)

ad1 = demo()
ad2 = demo(20,13)
ad1.add()
ad2.add()
