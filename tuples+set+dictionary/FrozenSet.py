#immutable version of set 
f=frozenset([1,2,3,4])
print(f)


#works with all read functions but wont work with write functions 
#2d set is possible 
fs=frozenset([1,2,frozenset[3,4]])  #2D

print(fs) 

##set comprehension
print({i for i in range(1,11)})
