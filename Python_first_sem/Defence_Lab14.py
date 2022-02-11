from typing import List
import random

def qsort(arr: List[int]) -> list:
    if len(arr) <= 1:
        return arr
    else:
        m = random.choice(arr)
        left = []
        right = []
        for i in arr:
            if i < m:
                left.append(i)
            else:
                right.append(i)
        return qsort(left) + qsort(right)

arr = [9132912931, 5, 6, 2, 888, -9, 94, 55, 1, 319, -9999, -23, 3, 9, 0, 8]
print(qsort(arr))