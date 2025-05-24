my_dict = {'name':'jhon wick','age':26}
 # my_dict[0]-------->>> it wont work indexing not allowed 
 
 

print(my_dict['name'])
print(my_dict['age'])

print(my_dict.get('name'))
print(my_dict.get('age'))


#adding key value pairs 
my_dict['wepon']='glock'
print(my_dict)

 
 #remove key value pair 
d={'name':'tyler','friend':'nike','profession':'hitman','age':'27','kills':'1000+'}
 
#pop
d.pop('friend')
print(d) 

#popitem()-----..>> last wala pair ht jayga 

d.popitem()
print(d)

#del ---->>> key value pair delete
del d['profession'] 
print(d)

#clear---->> sb saaf krdega 
#d.clear()
#print(d)


#################################operations#########################################################


#membership
print('tyler' in d)   # false cuz it works on key not values

#iteration
for i in d :
    print(i)
    
    
for i in d :
    print([i],d[i])    
    
    
    