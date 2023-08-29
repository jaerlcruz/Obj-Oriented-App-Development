import check_input
import random

# Names: Justine Cruz, Weibo Zhang
# Date: 8/23/2023
# Desc: Chooses a value from 1-100 and has user guess the number in 6 tries.


# Compare user input and value to see if too high/low. Reprompt user if not the right answer
def check_value(user, target):
  if user > target:
    return check_input.get_int_range("Too high! Guess again (1-100): ", 1, 100)
  elif user < target:
    return check_input.get_int_range("Too low! Guess again (1-100): ", 1, 100)
  else:
    target


def main():
  print("- Guessing Game -")
  val = random.randint(1, 100)

  first_guess = check_input.get_int_range(
    'I’m thinking of a number. Make a guess (1-100): ', 1, 100)

  tries = 1
  if first_guess == val:
    print(f'Correct! You got it in {tries} try.')
  else:
    # initialize the loop prompt cycle
    guess = check_value(first_guess, val)
    tries += 1
    while guess != val:
      tries += 1
      guess = check_value(guess, val)
    print(f'Correct! You got it in {tries} tries.')


main()
