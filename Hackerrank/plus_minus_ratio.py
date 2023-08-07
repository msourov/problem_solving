#!/bin/python3

import math
import os
import random
import re
import sys
def plusMinus(arr):
    N,Z,P=[i for i in arr if i<0 ],[i for i in arr if i==0],[j for j in arr if j>0]
    r = ["%.6f" % v for v in [len(P)/len(arr), len(N)/len(arr), len(Z)/len(arr)]]
    
    for i in r:
        print(i)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
