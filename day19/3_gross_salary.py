# salary calculation read basic salary and calculate gross salary based on:

#basic<= 20,000 -> HRA 20%, DA 50%
#basic<= 40,000 -> HRA 25%, DA 60%
#above 40,000 -> HRA 30%, DA 70%


basic =int(input("enter a salary: "))

if basic <= 20000:
    hra= basic*20/100
    da=basic*50/100

elif basic <=40000:
    hra=basic*25/100
    da=basic*60/100

else:
    hra=basic*30/100
    da=basic*70/100

gross_salary= basic + hra + da

print("gross salary: ",gross_salary)
