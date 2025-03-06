#login and indentation
email=input('enter Email')
password=input('enter the password')

if email=='karan@gmail.com' and password=='mahoolpurawavy':
 print('welcome')

elif email =='karan@gmail.com' and password !='mahoolpurawavy':  #else if hai veere!!!
 print('incorrect password')
 password=input('enter password again')
 if password =='mahoolpurawavy':
     print('welcome,finally!')
 else:
     print('tere bus ki nai oye ')
else:
    print('acess denied -->> ude utthe dekh uthe kon uthe mai')
