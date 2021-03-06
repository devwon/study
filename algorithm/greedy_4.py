#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    n = len(arr)
    p = {v : i for i,v in enumerate(arr)} # position
    
    for i in range(n):
        # if K is exhausted then break the loop
        if k == 0:
            break
        
        # if already sorted, don't need to swap
        if arr[i] == n-i:
            continue
        
        # temp value is ith largest value(n-i place value)
        temp = p[n-i]
 
        # Swap positions
        p[arr[i]] = temp
        p[n-i] = i
 
        # Swap ith largest value : value of ith place value
        arr[temp], arr[i] = arr[i], arr[temp]
 
        # decrement k after swap
        k -= 1
    
    return arr

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
