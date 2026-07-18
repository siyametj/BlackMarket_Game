import time
import os
try:
    from market import show_market, buy_item
except ImportError:
    print("Plese chack is all file in a folder or not.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    while True:
        clear_screen()
        print("-" * 40)
        print("THE UNDERWORLD EMPIRE v1.0")
        print("-" * 40)
        print("\n1. Russian Roulette")
        print("2. High-Low Betting")
        print("3. Black Market")
        print("4. Exit")
        print("-" * 40)

        choice = input("What do you want to do (1/2/3/4): ").strip()

        if choice == '1':
            time.sleep(1)
            os.system('python russian_roulette.py')

        elif choice == '2':
            print("\nCasino is open..")
            time.sleep(1)
            start_betting()

        elif choice == '3':
            show_market()
            buy_item()
            input("\nEnter for exit..")

        elif choice == '4':
            print("Bye see you soon")
            break

        else:
            print("Please enter 1, 2, 3 or 4")
            time.sleep(1.5)

if __name__ == "__main__":
    show_menu()
