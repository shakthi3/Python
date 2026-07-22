
budget = int( input("Enter your budget : "))

for i in range (3):
    veg = input("Enter vegetable name : ")
    price = int( input("Enter Price: "))

    if budget >= price:
        print("purchased")
        budget -= price
        print("Remaining Budget: " ,budget)
    else:
        print("Not enough money to buy")
        
print("shopping completed!")
