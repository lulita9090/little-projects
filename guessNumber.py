import random

print("Hi! Welcome to the Number Guessing Game.\nYou have 7 tries to guess the number. Let's start!")

lower_bound = int(input('Enter a lower bound: '))
top_bound = int(input('Enter a top bound: '))

print(f'Now guess the number between {lower_bound} and {top_bound}.')

random_number = random.randint(lower_bound, top_bound)
tries = 0
band = False
while tries < 7 and not band:
  tries += 1
  user_guess = int(input('Enter your guess: '))
  if user_guess == random_number:
    band = True
  elif user_guess < random_number:
    print('Too low! Try a higher number.')
  else:
    print('Too high! Try a lower number.')

if band:
  print(f'Congratulations!  The number is {random_number}. You guessed it in {tries} attempts.')
else:
  print(f'Sorry! The number was {random_number}. Better luck next time.')
      
