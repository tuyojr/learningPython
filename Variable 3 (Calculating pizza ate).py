

name1 = input("What is your name: ")
name2 = input("What is your name: ")
name3 = input("What is your name: ")

pizza = input("How many slices are there in the pizza box: ")
pizza_price = input("What is the price of the pizza: ")

percentage_ate_by_person_1 = input(name1 + ", What percentage of the pizza did you eat: ")
percentage_ate_by_person_2 = input(name2 + ", What percentage of the pizza did you eat: ")
percentage_ate_by_person_3 = input(name3 + ", What percentage of the pizza did you eat: ")

number_of_slices_ate_by_person1 = float(percentage_ate_by_person_1)*float(pizza)
number_of_slices_ate_by_person2 = float(percentage_ate_by_person_2)*float(pizza)
number_of_slices_ate_by_person3 = float(percentage_ate_by_person_3)*float(pizza)

price_paid_by_name1 = float(percentage_ate_by_person_1)*float(pizza_price)
price_paid_by_name2 = float(percentage_ate_by_person_2)*float(pizza_price)
price_paid_by_name3 = float(percentage_ate_by_person_3)*float(pizza_price)

print (name1 + ( " ate ") + str(number_of_slices_ate_by_person1) + (" slices of pizza and will pay ") + str (price_paid_by_name1) + ("$ for his meal.") )
print (name2 + ( " ate ") + str(number_of_slices_ate_by_person2) + (" slices of pizza and will pay ") + str (price_paid_by_name2) + ("$ for his meal.") )
print (name3 + ( " ate ") + str(number_of_slices_ate_by_person3) + (" slices of pizza and will pay ") + str (price_paid_by_name3) + ("$ for his meal.") )