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


def timeConversion(s:str) -> str:
    # Write your code here
    ampm = s[8:]
    print(ampm)
    s = s[:8]
    if s[:2] == '12' and ampm == 'AM':
        s = '00' + s[2:]
    elif s[:2] != '12' and ampm == 'PM':
        s = str(12 + int(s[:2])) + s[2:]
    print(s)
    return s


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # s = input()
    #
    # result = timeConversion(s)
    #
    # fptr.write(result + '\n')
    #
    # fptr.close()
    a = timeConversion("12:15:00AM")