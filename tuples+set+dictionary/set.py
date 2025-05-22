#empty set 
s=set() #right method
print(type(s))
s1={}   #wrong method 
print(type(s1))


#1d set 
s1={1,2,34,4}
print(s1)
#2D set is not possible------>>>set only contain immutable datatype and it is a mutable datatype what a [HIPPOCRAT!] 

#hetro 
s3={1,2.5,True,"hello",69}  
print(s3)   # true =1 so vo output se hat jayega kyunki DUPLICATES ARE NOT ALLOWED in SET!!!!!

s4={1,2.5,True,"hello",69,25.008,0.7}
print(s4)                #order is not retained as given kyunki background m hashing chalri h 



##### JAAAT PARIVARTAN ----->> TYPE CONVERSION
s5=set([4,5,7,6])
print(s5)







  ##############################Accessing / editing items dont work because Index hi nhi h ######################################################     
s={1,2,3,4,5}
#add
s.add(6)
print(s)

#update
s.update([7,8,9])
print(s)



###########Deleting###########
s.discard(6)  #vo particular element nikal do 
print(s)


s.remove(7)
print(s)


s.pop()  #randomly koi hi element hta dega 
print(s)

s.clear()  # pura set khali kr dega kuch nhi chorega --empty set bna dega 
print(s)


del(s)
print(s) #pura uda dega 



