#Number Guessing Game:

import random
from replit import clear
def guess_the_number():
  
  #print art logo
  from art import logo
  print(logo)
  
  print("Welcome to the Number Guessing Game!")
  print("I'm Thinking of number between 1 and 100")
  
  #to get random number
  number= random.randint(1,100)
  
  #to check the number you gussed
  def check_number():
    g_num=int(input("Make a Guess: "))
    if g_num==number:
      return 0
    elif g_num>number:
      print("Too high")
    elif g_num<number:
      print("Too low")
  
  #to ittirate the number of attempts with difficulty level
  def attempts(n):
    for i in range(n):
      cn= check_number()
      if cn==0:
        print(f"you have got it correct, the number is {number}")
        break
      else:
          print(f"you have {n-(i+1)} attempts remainig to guess the number")
    if cn!=0:
      print(f"you coudnt guess in given number of attempts. the number is {number}")
      
  difficulty = input("choose the difficulty level, Type 'easy' or 'hard': ").lower() 
  if difficulty=='easy':
    attempts(10)
  elif difficulty=='hard':
    attempts(5)
  else:
    print("wrong input")

check= True
while check:
  guess_the_number()
  c= input("This repl as ended do you want to run again?, Type 'y' or 'n': ").lower()
  if c=='y':
    clear()
    check = True
  elif c=='n':
    check = False
  else:
    print("wrong input")
    check= False
