print("Amount Due: 50")
amount_due = 50
while (amount_due > 0):
    coin_inserted = int(input("Insert Coin: "))
    if coin_inserted != 25 and coin_inserted != 10 and coin_inserted != 5:
        print("Amount Due:", amount_due)
        continue
    amount_due -= coin_inserted
    if amount_due > 0:
        print("Amount Due:", amount_due)
print("Change Owed:", 0 - amount_due)