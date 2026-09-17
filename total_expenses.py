import csv
import os

FILE_NAME = "expenses.csv"

def total_expenses():
    if not os.path.exists(FILE_NAME):
        print("\nNo expenses found.")
        return

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    total = sum(float(row["Amount"]) for row in rows)
    print(f"\nTotal spent: ₹{total:.2f}")

if __name__ == "__main__":
    total_expenses()
