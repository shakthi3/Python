n=int(input("enter a value"))
for i in range(0,n):
    for k in range(0,i):
        print(" ",end=" ")
    for j in range(0,n-i):
        print(" * ",end=" ")


    print( )
