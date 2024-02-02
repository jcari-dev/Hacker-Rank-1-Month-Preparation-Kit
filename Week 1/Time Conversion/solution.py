#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour = s[:2]

    if "AM" in s:

        if hour == "12":
            hour = "00"
        else:
            hour = hour.zfill(2)

    elif "PM" in s:

        if hour != "12":
            hour = int(hour) + 12
    
    # Remove AM/PM and the hour from string.
    s = s[2:-2]
    
    # String format the hour variable into the time string.
    military_time = f"{hour}{s}"
    
    return military_time
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
