#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    total = float(len(arr))
    pos = 0
    neg = 0
    for n in arr:
        if n > 0:
            pos +=1.
        elif n < 0:
            neg +=1.
    
    zero = total - pos - neg
    pos_ratio = pos/total
    neg_ratio = neg/total
    zero_ratio = zero/total
    
    print("%.6f" % pos_ratio)
    print("%.6f" % neg_ratio)
    print("%.6f" % zero_ratio)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
