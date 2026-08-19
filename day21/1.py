
# constructor
# __init__  it is automatically call


class demo():
    
    def __init__(self):

        self.a =100
        self.b=50

    def add(self):
        self.c= self.a+self.b
        print(" Addition : ",self.c)

ad = demo()
ad.add()


