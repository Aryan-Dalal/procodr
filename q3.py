import random as r
import math
from typing import NewType
import re

def mergeSort(array):
        if len(array) > 1:
            mid = len(array)//2

            L = array[mid:]
            R = array[:mid]

            mergeSort(L)
            mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1
 
            while j < len(R):
                array[k] = R[j]
                j += 1
                k += 1

arr = [12, 57, 39, 42, 20, 18]
new = (r.randint(1000000000, 9999999999))
new = [str(x) for x in str(new)]

sarr = [str(x) for x in arr]
print(sarr)
for j in range(len(sarr)):
    for i in range(10):
        sarr[j].replace(str(i), new[i])

print(sarr)
mergeSort(arr)
print(arr)
