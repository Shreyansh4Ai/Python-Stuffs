 #add 1 to 10 numbers in list 
l=[]
for i in range(1,11):
    l.append(i)

print(l)


#better Way
l= [i for i in range(1,11)]
print(l)