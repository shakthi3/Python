
for row in range(1,8):
    for col in range(1,8):
        if row+col==5 or col-row==3 or row-col==3 or row+col==11:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
        
     
