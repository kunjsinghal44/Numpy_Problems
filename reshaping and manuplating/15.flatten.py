# .ravel() - give view i.e effect array
# .flatten() - give copy only
# the methods used to convert multidim. arr to 1d arryay

import numpy as np

arr = np.array([[10,20,30],[40,50,60]])
print(arr.ravel())
print(arr.flatten())