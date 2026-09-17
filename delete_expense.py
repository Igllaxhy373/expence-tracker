import csv
import os

FILE_NAME = "expenses.csv"

def delete_expense():
    if not os.path.exists(FILE_NAME):
        print("\nNo expenses found.")
        return

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    if not rows:
        print("\nNo expenses found.")
        return

    for i, row in enumerate(rows, 1):
        print(f"{i}. {row['Date']} | {row['Category']} | "
              f"{row['Description']} | ₹{float(row['Amount']):.2f}")

    try:
        number = int(input("\nEnter expense number to delete (0 to cancel): "))
    except ValueError:
        print("Enter a valid number.")
        return

    if number == 0:
        return

    if not 1 <= number <= len(rows):
        print("Invalid expense number.")
        return

    deleted = rows.pop(number - 1)

    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Date", "Category", "Description", "Amount"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Deleted: {deleted['Description']} - ₹{float(deleted['Amount']):.2f}")

if __name__ == "__main__":
    delete_expense()
