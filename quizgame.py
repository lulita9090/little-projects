def quiz():
  print('Welcome to my game!')
  print('Answer the following questions:')
  '''''
  questions = [
    "1. What is the largest animal on Earth? ",
    "2. Which bird can fly backwards? ",
    "3. What is the only mammal capable of flight? "
  ]
  
  answers = [
    "blue whale",
    "hummingbird",
    "bat"
  ]
  
  score = 0
  
  for i in range(len(questions)):
    user_answer = input(questions[i]).strip().lower()
    if user_answer == answers[i]:
      print('Correct!')
      score += 1
    else:
      print('Incorrect!')
  
  print('\nQuiz completed!')
  print(f'You got {score}/{len(questions)} questions correct.')
  '''
  
  questions = [
    '1. What does CPU stand for? ',
    '2. What does GPU stand for? ',
    '3. What does RAM stand for? '
  ]
  
  answers = [
    'Central Processing Unit',
    'Graphics Processing Unit',
    'Ramdom Access Memory'
  ]
  
  score = 0
  
  for i in range(len(questions)):
    user_answer = input(questions[i]).strip().lower()
    if user_answer == answers[i].lower():
      print('Correct!')
      score += 1
    else:
      print('Incorrect!')
      
  print('\nQuiz completed')
  print(f'You got {score}/{len(questions)} questions right.')

quiz()