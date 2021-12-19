
def count_substring(string, sub_string):
  sub_string_length = len(sub_string)
  count = 0
  for i in range(len(string) - sub_string_length+1):
    if sub_string == string[i:i+sub_string_length]:
      count += 1
  return count
      

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
