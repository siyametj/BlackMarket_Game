# russian_roulette.py
import random
import time
from market import wallet, show_market, buy_item, inventory

# main data
total_time = 6 # total shoot time
player_time = 3 # player can use 3 time
computer_time = 3 # computer can use 3 time
computer_name = random.choice(['BRO', "AI", "Enemy"]) # random computer name

# display
print("Welcome Russian Roulette")
print("-"*40)
while True:
  user_name = input("Enter name: ")

  # 1.if not user enter anything this will not stop
  if not user_name:
    print("Plese enter your name\n")
    continue

  # 2.if user not give number or string in name
  if not user_name.isalnum():
    print(f"{user_name} is not supportable")
    print("Name must be contain number and string\n")
    continue

  # 3.if not name len between 2 and 10
  if not (2 <= len(user_name) <= 10):
    print(f"{user_name} is not supportable")
    continue

  break # finally break this loop

# display some data
print("\n---Display info---")
print(f"Your name:     {user_name}")
print(f"Opponent name: {computer_name}")
print(f"Bullet count:  {total_time}| {user_name} time: {player_time}| {computer_name} time: {computer_time}")
print("-"*40)
print() # a blank space

# game start
print("Game is loading.....")
print(f"Current Balance: ${wallet['money']}")
choice = input("Press 'M' to visit Black Market or 'Enter' to start game: ").upper()

if choice == 'M':
  show_market()
  buy_item()

time.sleep(2) # now slow time ,, TODO: after can change
while True: # main loop
  random_bullet = random.choice([1, 0]) # 1=orginal bullet, 0=blank
  # take a response from user
  response_to_start = input("Press enter to continue")
  # 1.If not enter
  print()

  print("-"*40)
  print(f"Attempt: {total_time}| {user_name} attempt: {player_time}| {computer_name} attempt: {computer_time}")
  print(f"{user_name} attempt")
  input("Plese take your gun")
  time.sleep(2)

  # game logic for user
  if random_bullet == 1: # if player die
    if "safety vest" in inventory:
      print("Good luck! Your 'Safety Vest' saved you.")
      inventory.remove("safety vest")
    else:
      print(f"{user_name} DIE")
      print(f"{computer_name} WIN\n")
      print("-"*40)
      break # main loop will stop

  else: # player not die
    player_time -= 1
    total_time -= 1
    print(f"{user_name} won this round")
    print(f"{user_name} attempt remain {player_time}\n")
    # it loop go down

  # computer time
  print(f"{computer_name} attempt")
  random_bullet = random.choice([1, 0]) # 1=orginal bullet, 0=blank
  time.sleep(2)
  if random_bullet == 1: # if player die
    print(f"{computer_name} DIE")
    print(f"{user_name} WIN\n")
    print("-"*40)
    break # main loop will stop

  else: # player not die
    print(f"Attempt: {total_time}| {user_name} attempt: {player_time}| {computer_name} attempt: {computer_time}")
    total_time -= 1
    computer_time -= 1
    print(f"{computer_name} won this round")
    print(f"{computer_name} attempt remain {computer_time}\n")
    print("-"*40)

  if total_time == 0:
    print("It's a draw")
    break

