#len/min/max/sorted

l=[2,1,5,7,0]

print(len(l)) #length 

print(min(l))

print(max(l))

print(sorted(l))  #sorting k liye asending and not permanent 

print(sorted(l,reverse=True))


#count
l=[1,2,1,3,4,1,5]

print(l.count(1 ))


#index
l=[1,2,1,3,2,5]
print(l.index(2))


#reverse
l=[2,1,5,7,0]
#permanently reverses the list 
l.reverse()

print(l)


#sort vs sorted
l=[2,1,5,7,0]
print(l)

print(sorted(l))  #temporary
print(l)

l.sort()  #permanent 
print(l)



#copy
l=[2,1,5,7,0]
print(id(l))

l1=l.copy()  #shallow copy --> naye address m list bna h but elements deep copied nai h so to nayi adress ki list still reference krti h purani list ko
print(l1)
print(id(l1))