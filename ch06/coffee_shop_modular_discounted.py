from transactions import *
from promotion import *

items = ["DONUT", "LATTE", "FILTER", "MUFFIN"]
prices = [1.50, 2.20, 1.80, 1.20]
running = True

while running:
        option = 1
        for choice in items:
            print(str(option) + ". " + choice)
            option = option + 1
        choice=int(input("Choose an option: "))
        if choice == option:
            running = False
        else:
            credit_card = input("Credit card number: ")
            new_price=discount(prices[choice -1])
            save_transaction(new_price, credit_card, items[choice -1])
