import json
import os
from datetime import date

FILENAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(FILENAME, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses):
    amount = float(input("Enter amount (₹): "))
    category = input("Enter category (Food/Travel/Shopping etc): ")
    note = input("Enter a short note: ")
    today = str(date.today())

    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": today
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n--- Your Expenses ---")
    for i, e in enumerate(expenses, 1):
        print(f"{i}. [{e['date']}] ₹{e['amount']} | {e['category']} | {e['note']}")

def total_expenses(expenses):
    total = sum(e["amount"] for e in expenses)
    print(f"\n💰 Total Spent: ₹{total}")

def main():
    expenses = load_expenses()
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_expenses(expenses)
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Try again.")

main()