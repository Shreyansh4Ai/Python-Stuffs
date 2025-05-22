s1={1,2,3,4,5}
s2={4,5,6,7,8}
#union  |
print(s1|s2)

 #intersection &
print(s1&s2)  

#difference
print(s1-s2)   # s1 me se s2 kcommon elements hta dooo
print(s2-s1)   #s2 me se s1 k common elements hta doo

#symmetric difference ^
print(s1 ^ s2) #common elements ko remove kr doooo

#Membership --->>> element exist krta h ki ni 
print(1  in s2)

#iteration
for i in s1:
    print(i)
    
    