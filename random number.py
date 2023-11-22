import random
def guess_number():
  randomNumber = random.randint(0,100)
  while True:
    guess = int(input("Guess the number (between 1 and 100): "))
    guess +=1

    if guess== randomNumber:
      print("You Guessed it")
      break
    elif guess < randomNumber:
      print("Too Low")
    else:
      print("Too High")
guess_number()
