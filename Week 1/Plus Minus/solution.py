#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    
    positive_count = 0
    negative_count = 0
    zero_count = 0

    for number in arr:
        if number == 0:
            zero_count += 1
        elif number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1

    arr_length = len(arr)

    positive_ratio = round(positive_count / arr_length, 6)
    negative_ratio = round(negative_count / arr_length, 6)
    zero_ratio = round(zero_count / arr_length, 6)

    print(f"{positive_ratio} \n{negative_ratio} \n{zero_ratio}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
