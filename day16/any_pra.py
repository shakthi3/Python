
data=["A","B","C","A","A"]

A=0
B=0
C=0

for i in data:
    
    if i=="A":
        A+=1
        
    elif i=="B":
        B+=1
        
    elif i=="C":
        C+=1
        
    else:
        print("Invalid input")
        
if A>B and A>C:
    print("A is winner")
    
elif B>C and B>A:
    print("B is winner")
    
elif C>A and C>B:
    print("C is winner")
else:
    print("Its tie")

