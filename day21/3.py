# notes- mro
# ambigous

class a():
    def one(self):
        print("one")
        
class b():
    def one(self):
        print("two")
        
class c(a,b):
    pass

show=c()
show.one()
b.one(show)