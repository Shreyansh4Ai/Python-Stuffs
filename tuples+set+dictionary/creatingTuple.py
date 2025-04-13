  #empty
t1=()
print (t1)

#create a tupple with single item
t2 =(2)
print(type(t2))   #not a tupple

#homo
t3 =(1,2,3,4,)
print(t3)

#hetero
t4=(1,2.5,True,[1,2,3])
print(t4 )

t5=(1,2,3,(4,5))  #2d tupple
print(t5)
#using type conversion
t6=tuple('hello')  #tuple is used for type conversion
print(t6)



#acessing tuples 
print(t3)
print(t3[0])
print(t3[-1])


#slicing
print(t3[::-1])
#reverse

print(t5[-1][0])
 


#editing items
#print(t3)
#t3[0]=100     #immutable

#deleting items
#print(t3 )
#del(t3)
#print(t3)

# del(t5[-1]) y list m chalta h but tupple pr nhi


