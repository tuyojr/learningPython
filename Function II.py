def person_1(name):
    print(name + " Welcome, what would you like to order?")
person_1("Cashier")

def person_2(name,food,drink,dessert):
    name = input("What is your name: ")
    food = input("What would you like to eat: ")
    drink = input("What would you like to drink: ")
    dessert = input("What would you like for dessert: ")
    print(name + ": I would like to order some " + food + ", and I would like to drink " + drink + ". Also, I would like some " + dessert + " for dessert. Thank you.")
person_2("name","food","drink","dessert")

def person_1_2(name):
    print(name + ": Your order has been placed. Kindly wait a moment while we get it ready... Here you go. Thank you for patronizing us.")
person_1_2("Cashier")

