# market.py

# Shared data across all game modules
inventory = []
wallet = {"money": 1000}  # Unified wallet starting at $1000

shop_items = {
    "safety vest": 1000,
    "lucky charm": 500,
    "fake id": 300,
    "aladin lamp": 5000
}

def show_market():
    print("-" * 40)
    print("Welcome To The Black Market")
    print(f"Your Balance: ${wallet['money']}")
    print("-" * 40)
    for item, price in shop_items.items():
        print(f"- {item}: ${price}")
    print("-" * 40)

def buy_item():
    item_name = input("Enter item name to buy: ").lower().strip()
    if item_name in shop_items:
        price = shop_items[item_name]
        if wallet['money'] >= price:
            wallet['money'] -= price
            inventory.append(item_name)
            print(f"\nSuccess! You bought a {item_name}.")
            print(f"Remaining balance: ${wallet['money']}\n")
            return True
        else:
            print("\nInsufficient money!")
            print(f"Your balance: ${wallet['money']} | Item price: ${price}\n")
            return False
    else:
        print("\nThis item is not in the store.\n")
        return False
