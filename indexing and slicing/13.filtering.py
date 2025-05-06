#also called boolean masking as it is based on conditions

import numpy as np

arr = np.array([10,20,30,40,50,60])

#print(arr[arr >25])
new_arr=arr[arr>25]
print(new_arr)