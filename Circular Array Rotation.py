#!/bin/python3

import math
import os
import random
import re
import sys
# 0 1 2 3 4 5 6 7 8 9 10 11 12
#10 11 12 0 1 2 3 4 5 6 7 8 9
#1 2 3
#2 3 1
# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
  k=k%len(a)
  result=[]
  for i in queries:
    if i >=k:
      result.append(a[i-k])
    else :
      result.append(a[len(a)-k+i])
  return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
