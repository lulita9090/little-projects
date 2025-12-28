import random

low = int(input('Enter the lower bound: '))
high = int(input('Enter the upper bound: '))

print(f'You have 7 chances to guess the number between {low} and {high}')

num = random.randint(low, high)
ch = 7
gc = 0

while gc <= ch:
  gc += 1
  guess = int(input('Enter your guess: '))
  
  if guess == num:
    print('Correct!')
    break
  elif gc >= ch and guess != num:
    print(f'Sorry, you lost! The guess was {num}.')

  elif guess < num: 
    print('Too low. Try a higher number.')
  else:
    print('Too high. Try a lower number.')