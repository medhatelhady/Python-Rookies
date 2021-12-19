#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
  temp1=scores[0]
  tepm2=0
  temp2=scores[0]
  count=[0,0]
  for i in scores:
    if i > temp1:
      temp1=i
      count[0]+=1
    elif i<temp2:
      temp2=i
      count[1]+=1
  return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
