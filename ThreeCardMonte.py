import random
import check_input
# Names: Justine Cruz, Weibo Zhang
# Date: 8/28/2023
# Desc: Three Card Monte: Player places a bet and guesses queen's location.


def get_users_bet(money):
  # Display user's money and get user bet (must be no more than how much money they have)
  print(f"You have ${money}.")
  return check_input.get_int_range("How much you wanna bet? ", 1, money)

def get_users_choice():
  # Display cards facing down, prompt user for guess
  print("""
+-----+ +-----+ +-----+
|     | |     | |     |
|  1  | |  2  | |  3  |
|     | |     | |     |
+-----+ +-----+ +-----+
""")
  return check_input.get_int_range("Find the queen: ", 1, 3)
  


def display_queen_loc(queen_loc):
  # given queen_loc, reveal queen's location.
  if queen_loc == 1:
    c1, c2, c3 = 'Q', 'K', 'K'
  elif queen_loc == 2:
    c1, c2, c3 = 'K', 'Q', 'K'
  else:
    c1, c2, c3 = 'K', 'K', 'Q'
  print(f"""
+-----+ +-----+ +-----+
|     | |     | |     |
|  {c1}  | |  {c2}  | |  {c3}  |
|     | |     | |     |
+-----+ +-----+ +-----+
""")
  
def game_result(choice, queen_loc):
  # returns boolean value based on if player has won or not.
  if choice == queen_loc:
    print("You got lucky this time...")
    return True
  else:
    print("Sorry... you lose.")
    return False

def main():
  # get_users_choice()
  # 1. Initializes user’s money.
  money = 100  #Player starts with $100.


  print('''-Three card Monte-\nFind the queen to double your bet!
  ''')
  while True:
    queen_loc = random.randint(1, 3)
    user_bet = get_users_bet(money)
    money -= user_bet
    user_guess = get_users_choice()
    display_queen_loc(queen_loc)
    is_win = game_result(user_guess, queen_loc)

    #  update money if win/loss
    if is_win: 
      money += user_bet * 2

    if not check_enough_money(money): 
      print('You\'re out of money. Beat it loser!')
      break
    elif not prompt_play_again(): 
      break
  
  print ('Game Over')
  

def prompt_play_again():
  return check_input.get_yes_no('Play again? (Y/n) ')

def display_money(money):
  print(f'You have ${money}.')

def check_enough_money(money):
  return money > 0

main()
