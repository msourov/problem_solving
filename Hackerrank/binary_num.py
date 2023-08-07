#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    bin_a = bin(n).split('b')[1]
    l = bin_a.split('0')
    print(len(max(l)))
