#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def LCM(a, b):
  factor = max(a,b)

  while not((factor % a == 0) and (factor % b ==0)):
    factor += 1
  return factor



  

def getTotalX(a, b):
  
  factor = LCM(a[0], a[-1])
  if len(a) == 3:
    factor = LCM(factor, a[1])
  first_factor = factor
  temp = min(b)
  is_factor = True
  count = 0
  while is_factor or factor <= temp:
    is_factor = True
    for i in b:
      is_factor = is_factor and (i%factor == 0)
    if is_factor:
      count += 1
    factor += first_factor
    
  return count
    

  

  
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
