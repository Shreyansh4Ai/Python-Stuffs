t1=(1,2,3)
t2=(4,5,6)

print(t1+t2)  #addition 
print(t1*5)  #multipliction

#membership ----->> determines whether the ite is available in the tuple or not 
print(1 in t1)
print( 6 in t2 )
print(0 in t1 ,t2)  #this will output false , t2 tuple elements 


#iteration
for i in t1+t2:
    print(i) 
for i in t1:
    print(i)
    
    
    
                 ################################# FUNCTIONS ############################################# 
t=(1,2,3,4,56,7)              
print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sorted(t))
print(sorted(t,reverse=True))      

#count --->> counts how many time a particuar element lies within the tuple 
print(t.count(5))      
print(t.count(50))  

#index --->> tells the index for the particular element 
print(t.index(3))
print(t.index(56))
   