#!/bin/python3

import math
import os
import random
import re
import sys
from typing import *
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr: list) -> None:
    # Write your code here
    positive_count = 0
    negitive_count = 0
    zero_count = 0

    for i in arr:
        if i > 0:
            positive_count += 1
        elif i < 0:
            negitive_count += 1
        else:
            zero_count += 1
    print("%.6f" % (positive_count/len(arr)))
    print("%.6f" % (negitive_count / len(arr)))
    print("%.6f" % (zero_count / len(arr)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
