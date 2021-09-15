#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    sum1, sum2 = 0, 0
    for index, row in enumerate(arr):
        sum1 += row[index]
        sum2 += row[len(arr)-1-index]
    return abs(sum1-sum2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
