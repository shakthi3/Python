# with argument, with return type

def check(n):
    
    if n%2==0:
        return "even"
    else:
        return "odd"

n= int(input("enter a value: "))
print(check(n))
