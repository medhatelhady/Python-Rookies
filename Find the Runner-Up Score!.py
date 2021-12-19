

"""Find the Runner-Up Score!"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    first_max = -100
    second_max = -100

    for i in arr:
      if i > second_max:
        if i > first_max:
          second_max = first_max
          first_max = i
        elif i < first_max:
          second_max = i
          
        
    print(second_max)
