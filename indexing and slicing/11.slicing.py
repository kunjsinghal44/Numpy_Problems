# start:stop:step
# arr[start:end], start to end -1

import numpy as np

arr = np.array([10,20,30,40,50,60])
print(arr[1:5]) #index 1 to 4
print(arr[:5])#index 0 to 4
print(arr[1:]) #index 1 to end
print(arr[1:5:2]) #index 1 to 4 with 2 steps
print(arr[::2]) #from index 0 to end with 2 steps
print(arr[::-1]) #reverse out the array