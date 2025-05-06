#used to add 2 arrays
# axis 0 > vertical stacking
# axis 1 > horizontal stacking

import numpy as np

arr1 = np.array([10,20,30,40])
arr2 = np.array([50,60,70,80])

new_arr = np.concatenate((arr1,arr2),axis=0)
print(new_arr)
#axis = 1 not work as this is 1d array