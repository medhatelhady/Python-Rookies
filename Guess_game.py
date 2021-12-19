import random

n_tries = 1  # store number of tries

# variable to pick a random number from 1 to 10
number = random.randint(1, 10)
      

# get the number that user enter
temp = int(input('Enter a number between 1 and 10 '))

''' if user enter the correct answer program print number of tries
if the number is wrong program ask user to try again until
he get the correct number'''

while(temp != number):
      temp = int(input('Wrong! try again '))
      n_tries += 1
      
print(n_tries)
