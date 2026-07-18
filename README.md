# 🕶️ The Underworld Empire (BlackMarket Game)

A text-based text adventure suite featuring criminal risk engine games, dynamic inventory purchases, and a shared persistent casino currency simulator. Built natively using modular Python layout architectures.

## 🎮 Main Features

* **Underworld Betting (High-Low):** Test your luck in a card counting gambling house. Try out **Double or Nothing** mechanics to scale up your cash stack, but watch out—going broke ends your run.
* **Black Market:** Buy items like the **Safety Vest** to tip the survival scale rules in your favor.
* **Russian Roulette:** The ultimate high-stakes gamble. Survive up to 6 unpredictable trigger pulls against an automated computer alias.

## 📁 Repository Map

* `main.py` - The game launch pad and execution engine menu interface.
* `market.py` - The global data storage containing your `wallet` ledger and shop metrics.
* `betting.py` - The logic rule processing behind the high-low card game.
* `russian_roulette.py` - The match handler for the survival round simulator.

## 🚀 How to Run

1. Open a terminal and navigate to the project root directory.
2. Run the program using Python 3:
   ```bash
   python main.py
