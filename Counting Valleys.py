#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    count=0
    step=0
    laststep=0
    for i in s:
        if i=='D':
            laststep=step
            step-=1
        elif i=='U':
            laststep=step
            step+=1
        if step==0 and laststep==-1:
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
