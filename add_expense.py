import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

def add_expense():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            csv.writer(file).writerow(["Date", "Category", "Description", "Amount"])

    print("\n--- Add Expense ---")
    category = input("Category: ").strip()
    description = input("Description: ").strip()

    while True:
        try:
            amount = float(input("Amount (₹): "))
            if amount > 0:
                break
            print("Amount must be greater than 0.")
        except ValueError:
            print("Enter a valid amount.")

    date = input("Date (DD-MM-YYYY) [Enter for today]: ").strip()
    if not date:
        date = datetime.now().strftime("%d-%m-%Y")

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        csv.writer(file).writerow([date, category, description, f"{amount:.2f}"])

    print("Expense added successfully!")

if __name__ == "__main__":
    add_expense()
