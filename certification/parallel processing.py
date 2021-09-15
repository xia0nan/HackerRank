#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minTime' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY files
#  2. INTEGER numCores
#  3. INTEGER limit
#

def minTime(files, numCores, limit):
    # Write your code here
    result = 0
    remaining = []
    for i in files:
        if i % numCores != 0:
            result += i
        else:
            remaining.append(i)
            
    if remaining:
        remaining.sort(reverse=True)
        for j in remaining:
            if limit > 0:
                result += j/numCores
                limit -= 1
            else:
                result += j
    return int(result)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    files_count = int(input().strip())

    files = []

    for _ in range(files_count):
        files_item = int(input().strip())
        files.append(files_item)

    numCores = int(input().strip())

    limit = int(input().strip())

    result = minTime(files, numCores, limit)

    fptr.write(str(result) + '\n')

    fptr.close()
