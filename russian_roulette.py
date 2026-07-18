# russian_roulette.py
import random
import time
from market import wallet, show_market, buy_item, inventory

def play_russian_roulette():
    total_time = 6
    player_time = 3
    computer_time = 3
    computer_name = random.choice(['BRO', "AI", "Enemy"])

    print("\n" + "="*40)
    print("WELCOME TO RUSSIAN ROULETTE")
    print("="*40)

    while True:
        user_name = input("Enter your criminal alias: ").strip()

        if not user_name:
            print("Please enter a name.")
            continue
        if not user_name.isalnum():
            print("Name must contain only numbers and letters.")
            continue
        if not (2 <= len(user_name) <= 10):
            print("Name length must be between 2 and 10 characters.")
            continue
        break

    print("\n--- Match Details ---")
    print(f"Your name:      {user_name}")
    print(f"Opponent name: {computer_name}")
    print(f"Total Chambers: {total_time} | Max Pulls -> {user_name}: {player_time}, {computer_name}: {computer_time}")
    print("-" * 40)

    print(f"Current Balance: ${wallet['money']}")
    choice = input("Press 'M' to visit Black Market before playing, or 'Enter' to start: ").upper().strip()

    if choice == 'M':
        show_market()
        buy_item()

    print("\nSpinning the cylinder...")
    time.sleep(1.5)

    while total_time > 0:
        random_bullet = random.choice([1, 0])  # 1 = Live, 0 = Blank

        input(f"\n[Round Remaining: {total_time}] Press Enter to pull the trigger against your head...")
        print("...")
        time.sleep(1)

        # Player Turn
        if random_bullet == 1:
            if "safety vest" in inventory:
                print("💥 *BANG!* The bullet hit! But your 'Safety Vest' absorbed the impact! It shreds to pieces.")
                inventory.remove("safety vest")
            else:
                print("💥 *BANG!* ...You died.")
                print(f"{computer_name} WINS.\n")
                break
        else:
            print("click... Clear! You survived.")
            player_time -= 1
            total_time -= 1

        if total_time <= 0:
            break

        # Computer Turn
        print(f"\n{computer_name} takes the revolver...")
        time.sleep(1.5)
        random_bullet = random.choice([1, 0])

        if random_bullet == 1:
            print(f"💥 *BANG!* {computer_name}'s brains are all over the wall.")
            print(f"{user_name} WINS!\n")
            break
        else:
            print("click... Clear! The opponent survived.")
            computer_time -= 1
            total_time -= 1

    if total_time == 0:
        print("\nThe gun is empty! It's a miracle draw.")
