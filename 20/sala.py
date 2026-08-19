#Salary Calculation

Basic=float(input("Enter Basic Salary:"))

if Basic<=20000:
    hra=Basic*20/100
    da=Basic*50/100
elif Basic<=40000:
    hra=Basic*25/100
    da=Basic*60/100
else:
    hra=Basic*30/100
    da=Basic*70/100

gross_salary=Basic+hra+da

print("Basic Salary:",Basic)
print("HRA:",hra)
print("DA:",da)
print("Gross Salary:",gross_salary)
