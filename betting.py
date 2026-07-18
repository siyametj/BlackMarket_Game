# betting.py
import random
import time
from market import wallet

def start_betting():
    print("-" * 40)
    print("WELCOME TO UNDERWORLD BETTING (HIGH-LOW)")
    print("-" * 40)

    while True:
        print(f"Your wallet: ${wallet['money']}")

        bet_input = input("How much do you want to bet? (or press 'E' to exit): ").strip()
        if bet_input.upper() == "E":
            print("Leaving the casino... Bye!")
            break

        if not bet_input.isdigit():
            print(f"Please enter a valid number, not '{bet_input}'")
            continue

        bet_amount = int(bet_input)

        if bet_amount > wallet['money']:
            print("Insufficient money!")
            print(f"Your balance: ${wallet['money']} | Bet amount: ${bet_amount}")
            continue

        current_number = random.randint(1, 13)
        print(f"\nCurrent Card number: {current_number}")
        print("Will the next card be (H)igher or (L)ower than this one?")

        guess = input("Your guess (H/L): ").upper().strip()

        if guess not in ["H", "L"]:
            print("Please enter H or L")
            continue

        next_number = random.randint(1, 13)
        print("Dealing card...")
        time.sleep(1.2)
        print(f"Next card is: {next_number}")

        win = False
        if guess == "H" and next_number > current_number:
            win = True
        elif guess == "L" and next_number < current_number:
            win = True

        if win:
            print(f"You win this round! You won ${bet_amount}.")
            choice = input("Double or Nothing? (D/N): ").upper().strip()

            if choice == "D":
                print("\nGoing for DOUBLE...")
                time.sleep(1)

                new_num = random.randint(1, 13)
                print(f"New base card: {new_num}")
                new_guess = input("Is the next one (H)igher or (L)ower? ").upper().strip()

                final_num = random.randint(1, 13)
                print(f"Result card: {final_num}")

                if (new_guess == "H" and final_num > new_num) or (new_guess == "L" and final_num < new_num):
                    wallet['money'] += (bet_amount * 2)
                    print(f"Congratulations! You doubled it. Balance: ${wallet['money']}\n")
                else:
                    wallet['money'] -= bet_amount
                    print(f"Unlucky! You lost everything from this bet. Balance: ${wallet['money']}\n")
            else:
                wallet['money'] += bet_amount
                print(f"Smart choice. Collected earnings. Balance: ${wallet['money']}\n")
        else:
            wallet['money'] -= bet_amount
            print(f"You lost this round! Lost ${bet_amount}. Balance: ${wallet['money']}\n")

        if wallet['money'] <= 0:
            print(f"You are completely broke! You cannot play anymore.")
            break
