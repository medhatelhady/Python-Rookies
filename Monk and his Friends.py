'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''


n = int(input())
for i in range(n):
    n, m  = map(int, input().split())
    arr = list(map(int, input().split()))

    n_list = set(arr[:n])


    for i in range(n, m+n):
        if arr[i] in n_list:
            print("YES")
        else:
            print("NO")
            n_list.add(arr[i])

    
