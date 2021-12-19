#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def count(ar1,ar2):
    n=0
    for i in range(len(ar1)):
        if ar1[i]=='1' or ar2[i]=='1':
            n+=1
    return n
def acmTeam(topic):
    temp=[]
  
    for i in range(len(topic)-1):
        for j in range(i+1,len(topic)):
            temp.append(count(topic[i],topic[j]))
    return [max(temp),temp.count(max(temp))]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
