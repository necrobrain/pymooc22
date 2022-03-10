# Write your solution here

times = int(input("How many times a week do you eat at the student cafeteria? "))
price = int(input("The price of a typical student lunch? "))
money = int(input("How much money do you spend on groceries in a week? "))

daily = (price * times / 7) + (money / 7)
weekly = price * times + money

print("Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")