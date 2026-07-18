# main.py
import time
import os
from betting import start_betting
from market import show_market, buy_item
from russian_roulette import play_russian_roulette

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    while True:
        clear_screen()
        print("-" * 40)
        print("THE UNDERWORLD EMPIRE v1.0")
        print("-" * 40)
        print("1. Russian Roulette (High Stakes Survival)")
        print("2. High-Low Betting (Casino Mini-game)")
        print("3. Black Market (Buy Protective Items)")
        print("4. Exit Game")
        print("-" * 40)

        choice = input("Select a venue (1/2/3/4): ").strip()

        if choice == '1':
            time.sleep(0.5)
            play_russian_roulette()
            input("\nPress Enter to return to the hideout...")

        elif choice == '2':
            print("\nEntering the backroom casino...")
            time.sleep(1)
            start_betting()
            input("\nPress Enter to return to the hideout...")

        elif choice == '3':
            clear_screen()
            show_market()
            buy_item()
            input("Press Enter to return to the hideout...")

        elif choice == '4':
            print("\nLeaving the Underworld Empire. Stay safe out there.")
            break
        else:
            print("Invalid input. Pick an option between 1 and 4.")
            time.sleep(1.2)

if __name__ == "__main__":
    show_menu()
