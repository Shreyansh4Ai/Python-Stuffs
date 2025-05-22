#list
a=[1,2,3]
b=a
a.append(4)

print(a)
print(b)   #baad mappend kra fir bhi vo change jo h vo b m agya 
 
#tuple
c=(1,2,3)
d=c
c=c+(4,)

print(c)
print(d)   # yha  c ka change c m rha h vo d m reflect nhi hua h 

