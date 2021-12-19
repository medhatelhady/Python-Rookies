n_elements = int(input('Enter a number of elements : '))

while(n_elements <0):
      n_elements = int(input('it has to be positive : '))


array = list(map(int, input().strip().split()))

def array_sum_1(array):
      total = 0
      for i in range(n_elements):
            total += array[i]

      return total

def array_sum_2(array):
      total = 0
      index = 0
      while(index < n_elements):
            total += array[index]
            index += 1

      return total


def array_sum_3(array, length):
      length -= 1
      if length >= 0:
            return array[length] + array_sum_3(array, length)
      else:
            return 0

print(array_sum_1(array))

print(array_sum_2(array))

print(array_sum_3(array, n_elements))

