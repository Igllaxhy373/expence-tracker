import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

def monthly_total():
    month = input("\nEnter month and year (MM-YYYY): ").strip()

    try:
        datetime.strptime(month, "%m-%Y")
    except ValueError:
        print("Invalid format. Example: 09-2026")
        return

    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    total = 0
    count = 0

    for row in rows:
        try:
            date = datetime.strptime(row["Date"], "%d-%m-%Y")
            if date.strftime("%m-%Y") == month:
                total += float(row["Amount"])
                count += 1
        except ValueError:
            pass

    print(f"\n--- Monthly Summary: {month} ---")
    print(f"Number of expenses: {count}")
    print(f"Total spent: ₹{total:.2f}")

if __name__ == "__main__":
    monthly_total()
