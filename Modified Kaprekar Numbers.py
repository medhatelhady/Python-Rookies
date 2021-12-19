#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def isKaprekar(number):
    square = str(number**2)
    small_length = len(str(number))
    long_square = len(square)
    first_number = square[:-small_length] or '0'
    second_number = square[-small_length:] or '0'
    return number == (int(first_number) + int(second_number))

def kaprekarNumbers(p, q):
    values =[]
    for i in range(p, q+1, 1):
        if(isKaprekar(i) == True):values.append(i)
    if len(values) == 0:
        print("INVALID RANGE")
    else:
        for i in values:
            print(i, end=" ")
            
    

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
