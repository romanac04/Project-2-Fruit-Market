print("Welcome to GC Fruit Market!")
name = input("What is your name?")
print(f"Welcome {name}. Which fruit would you like to buy?")
fruit_options = ["Apple","Grape","Orange"]
fruit_prices = [2, 1, 3]
total_sales = 0
apple = 0
grape = 0
orange = 0

print(f"1.{fruit_options[0]} ${fruit_prices[0]}")
print(f"2.{fruit_options[1]} ${fruit_prices[1]}")
print(f"3.{fruit_options[2]} ${fruit_prices[2]}")
fruit_choice = int(input())
if fruit_choice == 1:
    total_sales += fruit_prices[0]
    apple += 1
    print(f"You bought a {fruit_options[0]} at ${fruit_prices[0]}.")
elif fruit_choice == 2:
    total_sales += fruit_prices[1]
    grape += 1
    print(f"You bought a {fruit_options[1]} at ${fruit_prices[1]}.")
elif fruit_choice == 3:
    total_sales += fruit_prices[2]
    orange += 1
    print(f"You bought a {fruit_options[2]} at ${fruit_prices[2]}.")
else:
    print("Have a great day!")
while True:
    print("Would you like to buy another piece of fruit? yes/no")
    response = input()
    if response == "yes":
        print(f"Welcome {name}. Which fruit would you like to buy?")
        print(f"1.{fruit_options[0]} ${fruit_prices[0]}")
        print(f"2.{fruit_options[1]} ${fruit_prices[1]}")
        print(f"3.{fruit_options[2]} ${fruit_prices[2]}")
        fruit_choice = int(input())
        if fruit_choice == 1:
            total_sales += fruit_prices[0]
            apple += 1
            print(f"You bought a {fruit_options[0]} at ${fruit_prices[0]}.")
        elif fruit_choice == 2:
            total_sales += fruit_prices[1]
            grape += 1
            print(f"You bought a {fruit_options[1]} at ${fruit_prices[1]}.")
        elif fruit_choice == 3:
            total_sales += fruit_prices[2]
            orange += 1
            print(f"You bought a {fruit_options[2]} at ${fruit_prices[2]}.")
    else:
        print(f"Order for {name}.")
        print(f"{apple} of {fruit_options[0]} at {fruit_prices[0]} apiece.")
        print(f"{grape} of {fruit_options[1]} at {fruit_prices[1]} apiece.")
        print(f"{orange} of {fruit_options[2]} at {fruit_prices[2]} apiece.")
        print(f"Subtotal is {total_sales}")
        tax = total_sales * .5
        print(f"Tax is {tax}")
        total = tax + total_sales
        print(f"Total is {total}")
        break
