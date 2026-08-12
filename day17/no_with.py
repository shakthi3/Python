# no argument, with return type

def check():
    n=int(input("enter a value: "))

    if n%2==0:
        return "even"
    else:
        return "odd"
print(check())
