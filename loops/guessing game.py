#generate a integer between 1 and 100
import random
jackpot=random.randint(1,100)

guess=int(input('guess kro'))

counter =1
while guess!=jackpot:
    if guess<jackpot:
        print('wrong! guess higher')
    else:
        print('wrong! guess lower')

    guess=int(input('guess kro'))
    counter +=1

else :
 print('correct guess')
 print('attempts',counter)