# write a program for ladder if else, nested if else and match case
# nested if else

hall_ticket = input("Enter you have a hall ticket : yes / no :")


if hall_ticket == "yes":

    stationary = input("Enter you have a stationary : yes / no :")
    
    if stationary == "yes" :
        print ( " you are allow for exam ")

    else :
        print ( " Stationary things is mandatory ")

else:
    print( " hall ticket is mandatory ")
