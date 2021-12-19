
n = int(input('inter a number bigger than 2 : '))

while(n<2):
      n = int(input('enter a valid number :'))
'''
function to check if a number is prime or not

it take an integer as paratemter

return false if number is not true

return True if number isprime
'''

def is_prime(num):
      for i in range(2, num):
            if num % i == 0:
                  return False
      return True

count = 0
i = 2
while count<1000 and i < n:
      if(is_prime(i)):
            print(i, end = " ")
            count += 1
      i += 1
      
print()
print(count)
            

            



