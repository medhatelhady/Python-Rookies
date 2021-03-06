#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
#Medhat elhady
def climbingLeaderboard(scores, alice):
  j=0
  n_order=list()
  scores = list(dict.fromkeys(scores))
  scores.sort()
  for i in alice:
    while j<len(scores) and i>=scores[j] :
      j=j+1
    n_order.append(len(scores)-j+1)  
  return n_order  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
