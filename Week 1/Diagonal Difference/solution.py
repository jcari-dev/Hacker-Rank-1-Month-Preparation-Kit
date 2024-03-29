#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here

    # The very quick and dirty way of traversing an array from left to right
    left_to_right = [arr[i][i] for i in range(len(arr))]
    # same here right ot left
    right_to_left = [arr[i][len(arr)-i-1] for i in range(len(arr))]
    
    return abs(sum(left_to_right) - sum(right_to_left))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
