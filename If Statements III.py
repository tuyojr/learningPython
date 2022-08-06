

p1_name = input("What is your name: ")
p1_wallet = input("How many $ONE do you have: ")

p2_name = input("What is your name: ")
p2_wallet = input("How many $ONE do you have: ")

p3_name = input("What is your name: ")
p3_wallet = input("How many $ONE do you have: ")

if float(p1_wallet) > float(p2_wallet) and float(p1_wallet) > float(p3_wallet):
    print(p1_name + " is the richest.")
elif float(p2_wallet) > float(p1_wallet) and float(p2_wallet) > float(p3_wallet):
    print(p2_name + " is the richest.")
elif float(p3_wallet) > float(p1_wallet) and float(p3_wallet) > float(p2_wallet):
    print(p3_name + " is the richest.")

