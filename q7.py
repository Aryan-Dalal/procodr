import math
import numpy as np
arr1 = [2, 3, 5, 8]
arr2 = [-12, -10, -6, -3, 4, 10]

for i in arr2:
    arr1.append(i)
    arr1.sort()
ans = np.median(arr1)
ans = math.ceil(ans)
print(ans)