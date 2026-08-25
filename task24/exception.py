# create a code for user defined exception scenerio

class AgeException(Exception):
    pass

age=int(input("enter your age: "))

try:
    if age>=18:
        print("you can vote")

    else:
        raise AgeException("your are not Eligible to vote")

except AgeException as ex:
    
    print(ex)

print("thank you")
