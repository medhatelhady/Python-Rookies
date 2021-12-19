#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#

def pageCount(n, p):
    if p%2==0:
        p+=1
    x=range(1,p,2)
    z=range(p,n,2)
    return min(len(x),len(z))
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
