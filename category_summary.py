import csv
import os

FILE_NAME = "expenses.csv"

def category_summary():
    if not os.path.exists(FILE_NAME):
        print("\nNo expenses found.")
        return

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    summary = {}
    for row in rows:
        category = row["Category"]
        summary[category] = summary.get(category, 0) + float(row["Amount"])

    print("\n--- Category Summary ---")
    for category, amount in sorted(summary.items()):
        print(f"{category:<20} ₹{amount:.2f}")

if __name__ == "__main__":
    category_summary()
