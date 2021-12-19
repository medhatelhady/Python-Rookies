#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
  i = 0
  j = 0
  test = 'hackerrank'
  while i < len(s) and j < len(test):
    if s[i] == test[j]:
      j += 1
    i += 1
  
  if j == 10:
    return 'YES'
  return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
