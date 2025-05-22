s={3,4,7,8,9,56,32,10,1}
print(len(s))
print(sum(s))
print(min(s))
print(max(s))
print(sorted(s))  # will give the result always in list format 

s2={76,5,26,34,22,1,2,3}
#union /update
print(s.union(s2))

s.update(s2)      #s2 k elements s m dl do 
print(s)       
print(s2)

#intersection/intersection_update
s1={1,2,3,4}
s3={4,5,6,8}
print(s1.intersection(s3)) #dono m common joh usse output krega 


print(s1.intersection_update(s3)) #  s1 and s3 m jo common elemnt h vhi sirf rhega s1 m baki del .....

print(s1)
print(s3)



#difference/difference_update
a={1,2,3,4,5}
b={2,1,3,9,0}
print(a.difference(b))  # a ke unique elements 
print(b.difference(a))  #  b ke unique elements

a.difference_update(b)
print(a)            #common elements nikal fekoon a ke 
print(b)      

#symmetric diff /symmetric_difference_update

x={1,2,3,4,5}
y={4,5,6,7,8}

print(x.symmetric_difference(y)) # x and y me se dono k bich ka common elemnt hta do 
print(x)
print(y)

x.symmetric_difference_update(y)
print(x)  # x se common element hta diye
print(y)




#isdisjoint / issubset / issuperset
l={1,2,3}
m={3,4,5}
print(l.isdisjoint(m))
print(l.issuperset(m))
print(l.issubset(m))


#copy
x={4,5,6,7}
w=x.copy()  #shallow copy
print(w)