#Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
#Salary(Lakhs) : Tax(%)
#Below 5 : 0%
#5-10 : 10%
#10-20 : 20%
#aboove 20 : 30%

a=int(input("ENTER SALARY:"))
if a<=500000:
    print("salary is",a)
elif a>500000 and a<1000000:
    a=a-(0.1*a)
    print("salary is", a)
elif a>1000000 and a<2000000:
    a=a-(0.2*a)
    print("salary is", a)
elif a>=2000000:
    a=a-(0.3*a)
    print("salary is", a)
else:
    print("invalid data")
