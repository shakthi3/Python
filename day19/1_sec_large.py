# second largest no.
# read three different no. and find the second largest number using if-else type.

a=int(input("enter a value : "))
b=int(input("enter a value : "))
c=int(input("enter a value : "))

if a>b  and a>c:
    if b>c:
        second=b
    else:
        second=c
else:
    if b>c:
        if a>c:
            second=a
        else:
            second=c
    else:
        second=b
print("second largest: ", second)
