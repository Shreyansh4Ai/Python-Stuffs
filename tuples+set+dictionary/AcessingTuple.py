#two ways 1) indexing   2) slicing 

t=(1,2,3,4,5,6,7,8)
print(t[0])

print(t[5])
print(t[-1]) #reverse


#slicing 

print(t[1:5:1])   # starting element included h and last element included nh h 
print(t[0:7:1])

#reverse ----->> hack left side wala number always bada hoga 
print(t[: : -1])
print(t[-1:-5:-1])



  ### Editting is not possible cuz immutable hai 
   ### same for adding 
   
   #deleting 
del(t)
print(t)  #error mtlb successfully deleted 
   