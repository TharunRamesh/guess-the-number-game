#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from replit import clear
def guess_the_number():
  from art import logo
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm Thinking of number between 1 and 100")
  number= random.randint(1,100)
  def check_number():
    g_num=int(input("Make a Guess: "))
    if g_num==number:
      return 0
    elif g_num>number:
      print("Too high")
    elif g_num<number:
      print("Too low")
  
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
