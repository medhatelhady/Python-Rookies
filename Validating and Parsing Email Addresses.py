
import re
n = int(input())

emails = [input() for i in range(n)]

for email in emails:
  if re.findall('<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>', email):
    print(email)
