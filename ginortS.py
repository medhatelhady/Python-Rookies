
# Enter your code here. Read input from STDIN. Print output to STDOUT

s = input()

def str_value(c):
  if c.isnumeric(): 
    if ord(c) %2 == 0:
      return ord(c) + 192
    else:
      return ord(c) +182
  elif c >= 'A' and c <= 'Z':
    return ord(c) +60
  return ord(c)


print(''.join(sorted(s, key = str_value)))



