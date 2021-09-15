#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if s[-2:] == "PM" and s[:2] != '12':
        new_s = str((int(s[:2]) + 12) % 24) + s[2:-2]
    elif s[-2:] == "AM" and s[:2] == '12':
        new_s = "00" + s[2:-2]
    else:
        new_s = s[:-2]
    return new_s 

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
