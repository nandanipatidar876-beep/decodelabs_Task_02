# Project 2: Expense Tracker
# Created By: Nandani Patidar

expenses = {}
total = 0

n = int(input("How many expenses do you want to enter? "))

for i in range(n):
    item = input(f"\nEnter expense name {i+1}: ")
    amount = float(input(f"Enter amount for {item}: ₹"))

    expenses[item] = amount
    total += amount

print("\n------ Expense Summary ------")

for item, amount in expenses.items():
    print(f"{item} : ₹{amount}")

print("-----------------------------")
print(f"Total Expense = ₹{total}")