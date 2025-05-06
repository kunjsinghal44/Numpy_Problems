# np.insert(array,index,value,axis=None)
# none for 1d , 0 for row in 2d , 1 for column in 2d 

import numpy as np

arr = np.array([10,20,30,40,50,60])
print(arr)
new_arr = np.insert(arr,2,25)
print(new_arr)
