import numpy as np # type: ignore

#0 D array
arr = np.array(24)
print(arr)

#1D array
ar=np.array([1,2,3,4,5,6,7])
print(ar)

#2D array
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1)

#3D array
arr3=np.array([[[1,2,3],[9,8,7],[4,5,6]]])
print(arr3)


#dimension check
print(arr.ndim )
print(ar.ndim)
print(arr1.ndim)
print(arr3.ndim)
#all verified and correct 

#miscellaneous 
arr4=np.array([[[[[[1,3,45],[123,355,0],[5,46,78]]]]]])
print(arr4)
print(arr4.ndim)