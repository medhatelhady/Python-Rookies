
number = int(input())

first = 0

second = 1

print(first, end = ' ')
print(second, end = ' ')

third = 0

for i in range(number - 2):
      third = first + second
      print(third, end = ' ')

      first = second
      second = third
