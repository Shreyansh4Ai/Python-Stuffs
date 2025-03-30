#scalar multiplication on a vector 
v=[2,3,4]
s=-3
#print(v*s)  #output empty list 

x=[]
for i in v:
    x.append(i*s)

print(x)    


#better way
print([s*i for i in v])