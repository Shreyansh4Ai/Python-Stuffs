#del
l=[1,2,3,4,5]
print(l)
del l[-1] #indexing 
print(l)

del l[1:3] #slicing
print(l)


#remove 

l=[1,2,3,4,5,6,7]
l.remove(5)

print(l)  


#pop
l=[1,2,3,4,5]

l.pop(0)
l.pop() #index not provided then vo last item ko delete kr deta h
print(l)


#clear--->> full deletion of list 
l=[1,2,3,4,5]
l.clear()
print(l)