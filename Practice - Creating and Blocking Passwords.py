
your_password = "Adedolapo1$"
your_answer = ""
number_of_tries = 0
number_of_max_tries = 5
max_tries = "Not reached"

while your_answer != your_password and max_tries != "Max tries reached.":
    if number_of_tries < number_of_max_tries:
        your_answer = input("What is your password: ")
        number_of_tries = number_of_tries + 1
    else:
        max_tries = "Max tries reached."

if max_tries == "Max tries reached.":
    print("Your account has been suspended.")
else:
    print("Log in successful.")
