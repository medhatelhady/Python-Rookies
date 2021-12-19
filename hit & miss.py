import random

gen =[str(random.randint(0, 9)) for i in range(3)]

guess = input()

hit = 0
mis = 0
for i in range(3):
      if guess[i] == gen[i]:
            hit += 1
      elif guess[i] in gen:
            mis += 1

print(hit, ' hti ',mis, ' mis') 



