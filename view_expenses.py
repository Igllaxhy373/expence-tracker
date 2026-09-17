import csv
import os

FILE_NAME = "expenses.csv"

def view_expenses():
    print("\n--- All Expenses ---")
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    if not rows:
        print("No expenses found.")
        return

    print(f"{'No.':<5}{'Date':<15}{'Category':<15}{'Description':<25}{'Amount':>12}")
    print("-" * 72)

    for i, row in enumerate(rows, 1):
        print(f"{i:<5}{row['Date']:<15}{row['Category']:<15}"
              f"{row['Description'][:24]:<25}₹{float(row['Amount']):>10.2f}")

if __name__ == "__main__":
    view_expenses()
