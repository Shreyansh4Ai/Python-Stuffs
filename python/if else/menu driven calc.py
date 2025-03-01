fnum =int(input('enter the 1st number'))
snum =int(input('enter second number'))

op=input('Enter the operation')

if op=='+':
    print(fnum + snum)

elif op =='-' :
    print(fnum-snum)

elif op == '*' :
    print(fnum *snum)

elif op == '/':
    print(fnum / snum)
else :
    print('enter a valid operator')



    #menu driven calculator

menu = input ("""
   HI! how can i help you .
   1. enter 1 for pin change
   2. enter 2 for balance check 
   3. enter  3 for withdrawal
    4. enter 4 for exit 
    """)

if menu == '1':
    print('pin change')

elif menu == '2' :
    print(' balance $$$$$$')

elif menu == '3' :
    print('withdrawal')

elif menu == '4' :
    print('exit')
