# adding method , give 0 to stop

total=0

while True:
    n=int(input("enter a value: "))
    if(n==0):
        break
    else:
        total=total+n
        print("current total: ",total)
print("final total: ",total)
