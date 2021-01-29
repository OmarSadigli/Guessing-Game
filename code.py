import random


print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100...")

random_number = random.randint(1,100)
level = input("Choose the Difficulty level. Type 'easy' or 'hard': ")

is_game_over = False
attempts = 0

def out_of_guesses():
  print("Too high")
  print("You have run out of guesses, you lose")
  is_game_over = True


if level == 'easy':
  attempts = 10
  print(f"You have {attempts} attempts remaining to guess the number.")
elif level == 'hard':
  attempts = 5
  print(f"You have {attempts} attempts remaining to guess the number.")

while not is_game_over and attempts > 0:
  guess = int(input("Make a guess: "))
  if guess > random_number and attempts > 0:
    attempts -= 1
    if attempts == 0:
      out_of_guesses()
    else:
      print("Too high.\nGuess again.")
      print(f"You have {attempts} attempts remaining to guess the number.")
  elif guess < random_number and attempts > 0:
    attempts -= 1
    if attempts == 0:
      out_of_guesses()
    else:  
      print("Too low.\nGuess again.")
      print(f"You have {attempts} attempts remaining to guess the number.")
  else:
    print(f"You got it! The answer was {random_number}")
    is_game_over = True
