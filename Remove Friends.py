'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

for i in range(int(input())):
    n, k = map(int, input().split())
    friends = map(int, input().split())


    stack = []
    for i in friends:
        while k and stack and stack[-1] < i:
            stack.pop()
            k -= 1
        stack.append(i)
    for i in stack:
        print(i, end=' ')
    print()    


            
