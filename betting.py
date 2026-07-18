import random
import time

money = 1000

def start_betting():
  global money
  print("-"*40)
  print("WELCOME TO UNDERWORLD BETTING")
  print("-"*40)

  while True:
    print(f"Your wallet: {money}")

    beat_input = input("How much do you want to bet? (or press 'E' to exit)")
    if beat_input.upper() == "E":
      print("Bye, see you soon!")
      break

    if not beat_input.isdigit():
      print(f"Plese enter a number. Not {beat_input}")
      continue

    bet_amount = int(beat_input)

    if bet_amount >  money:
      print("insufficient money")
      print(f"Your balance: ${money}")
      print(f"Beat amount: ${bet_amount}")
      continue

    current_number = random.randint(1, 13)
    print(f"Card number : {current_number}")
    print("Will the next card be (H)igh or (L)ow than this one?")

    guess = input("Your guess(H/L): ").upper().strip()

    if guess not in ["H", "L"]:
      print("Please enter H or L")
      continue
    next_number = random.randint(1, 13)
    print("Game start...")
    time.sleep(1.5)
    print(f"Next card is: {next_number}")

    win = False
    if guess == "H" and next_number > current_number:
      win = True
    elif guess == "L" and next_number < current_number:
      win = True

    if win:
      print("You win this game.")
      print(f"You get ${bet_amount} and your present balance is ${money}")

      choice = input("Double or Nothing? (D/N): ").upper().strip()

      if choice == "D":
        print("You are try to get 'Double'.")
        time.sleep(1)

        new_num = random.randint(1, 13)
        print(f"New card: {new_num}")

        new_guess = input("Is the next one (H)igh or (L)ow? ").upper().strip()
        final_num = random.randint(1, 13)

        print(f"Result: {final_num}")

        if (
          new_guess == "H" and final_num > new_num
        ) or (
          new_guess == "L" and final_num < new_num
        ):
          money += (bet_amount * 2)
          print(f"Congratuations you get double money. Your balance is ${money}")
        else:
          money -= bet_amount
          print(f"You loss ${bet_amount} and your balance is ${money}")
      else:
        money += bet_amount
        print(f"You save your moey and get {bet_amount}. Your balance is {money}")


    else:
      money -= bet_amount
      print("You loss this game.")
      print(f"You loss ${bet_amount} and your present balance is ${money}")

    if money <= 0:
      print(f'You cant play this game. Your balance is ${money}')
      break
      