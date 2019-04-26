"""
Project Euler #2: Even Fibonacci numbers

https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem
"""

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    fibo_list = [1,2,3]
    result = 2
    while fibo_list[2] < n:
        if fibo_list[2] % 2 == 0:
            result += fibo_list[2]
    
        fibo_list[0] = fibo_list[1]
        fibo_list[1] = fibo_list[2]
        fibo_list[2] = fibo_list[0] + fibo_list[1]
        
    print(result)
