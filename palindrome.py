# palindrome or not 

no = int(input("enter a num : "))
s= 0
temp = no

while no > 0:

    r = no % 10
    s = s+r

    if no >9:
        s=s*10
    no = no // 10

if( temp == s):
    print("it is palindrome ")
else :
    print(" it is not plaindrome")
