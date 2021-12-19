import re
# regex

def is_valid(password):
      length = len(password)
      if length < 6 or length > 20:
            return False
            
      if not re.search('[A-Z]', password):
            return False
      
      if not re.search('[a-z]', password):
            return False
      
      if not re.search('[0-9]', password):
            return False
      
      if not re.search('[@#%$&]', password):
            return False
      
      return True

n = int(input())

passwords = [input() for i in range(n)]


for password in passwords:
      if is_valid(password):
            print('valid')
      else:
            print('Not valid')


