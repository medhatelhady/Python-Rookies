'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from collections import Counter
n = int(input())

for i in range(n):
    s = input()
    t = input()

    s_count = Counter(s)
    t_count = Counter(t)
    print(sum((s_count - t_count).values()) + sum((t_count - s_count).values()))
