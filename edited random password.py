import random as rd

def generate_password():
      password = ''
      for i in range(4):
            password += rd.choice('abcdefghijklmnopqrstuvwxyz')
            password += rd.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
      
      password += rd.choice('@#$%&')
      password += rd.choice('123456789')
      password = [i for i in password]
      rd.shuffle(password)
      return ''.join(password)

for i in range(100):
      print(generate_password())
