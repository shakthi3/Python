# write a program for ladder if else, nested if else and match case
#match case

fruit = input ("Enter a fruit (apple, mango, orange) : ")

match fruit:
    case "apple" :
        print("apple cost : 100 ")
    case "mango":
        print("mango cost : 80 ")
    case "orange" :
        print(" orange cost : 60 ")
    case _:
        print(" fruit are not available ")
    
