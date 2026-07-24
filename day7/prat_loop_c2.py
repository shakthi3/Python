# print 1 2 30 4 5 60 7 8 90

num = 1

while num <10:

    if num%3==0 :   
        print(num*10)
        num+=1

    if not(num% 3==0) :
        print(num)
        num+=1
    if num ==9:
        print(num*10)
        break
    
    
 
