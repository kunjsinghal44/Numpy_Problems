#to check data type of elements

#import numpy as np
#arr_2d = np.array([[1,2,3],[4,5,6]])
#print(arr_2d.dtype)

#to change data type 

import numpy as np
arr_2d = np.array([[1,2,3],[4,5,6]])
float_arr = arr_2d.astype(float)
print(float_arr)
print(float_arr.dtype)