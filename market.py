# market.py

inventory = []
shop_items = {
  "safety vest": 1000,
  "lucky charm": 500,
  "fake id": 300,
  "aladin lamp": 5000
}

wallet = {"money": 500}

def show_market():
  print("-"*40)
  print("Welcome To Black Market")
  print(f"Your Balance: {wallet['money']}$")
  print("-"*40)

  for item, price in shop_items.items():
    print(f"- {item}: ${price}")
  print("-"*40)

def buy_item():
  print("-"*40)
  item_name = input("Enter item name: ").lower().strip()
  if item_name in shop_items:
    price = shop_items[item_name]
    if wallet['money'] >= price:
      wallet['money'] -= price
      inventory.append(item_name)
      print(f"Success! You bought {item_name}.")
      print(f"Remaining balance: ${wallet['money']}")
      return True

    else:
      print("Insufficient money")
      print(f"Your balance: ${wallet['money']}")
      print(f"Item price: ${price}")
      return False

  else:
    print("This item not in store")
    return False
