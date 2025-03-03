#triangle possibility
a=input("enter the first side")
b=input("enter the second side")
c=input("enter the third side")

if(a+b>c and a+c>b and b+c>a) :
    print("triangle formation is possible ")

else:
    print("triangle formation is not valid")
