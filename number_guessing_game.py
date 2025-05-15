
import random

def random_number():
    return random.randint(1, 10)

def main():
    number = random_number()
    while True:
      guest = int(input("Guess a number between 1 and 10: "))
      if number == guest:
          print(f"You guessed correctly!, the number was {number}")
          play_again = input("Do you want to play again? (y/n): ")
          if play_again.lower() == "y":
              number = random_number()
              continue
          else:
              print("Thank you for playing!")
              break
      elif guest > number:
          print("You guessed too high!")
      elif guest < number:
          print("You guessed too low!")

main()


  
        