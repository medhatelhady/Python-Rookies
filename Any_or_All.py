
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

arr = list(map(int, input().split()))

def is_palindrome(n):

  return any([n<10, n % 11 == 0])


print(all([any([is_palindrome(i) for i in arr])] + [i>0 for i in arr]))


