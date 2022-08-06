
def question():
    rules = input("You need to answer every question with Yes/No. Do you understand: ")
    if rules != "Yes":
       return print("Try again.")
    else: print("Next question.")
    Q1 = input("Are you hungry: ")
    if Q1 !="Yes":
        return print("Then, lets go play video games.")
    else: print("Next quetion.")
    Q2 = input("Do you wanna go eat somewhere: ")
    if Q2 != "Yes":
        return print("Let's go eat at my place.")
    else: print("Next question.")
    Q3 = input("Do you want to eat pizza: ")
    if Q3 != "Yes":
        return print("Let's go have burgers")
    else: print("Let's have pizza.")
    
question()
