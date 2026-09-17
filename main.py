import add_expense
import view_expenses
import total_expenses
import category_summary
import monthly_total
import delete_expense

def main():
    while True:
        print("\n" + "=" * 40)
        print("        PERSONAL EXPENSE TRACKER")
        print("=" * 40)
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Expenses")
        print("4. Category Summary")
        print("5. Monthly Total")
        print("6. Delete Expense")
        print("7. Exit")
        print("=" * 40)

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_expense.add_expense()
        elif choice == "2":
            view_expenses.view_expenses()
        elif choice == "3":
            total_expenses.total_expenses()
        elif choice == "4":
            category_summary.category_summary()
        elif choice == "5":
            monthly_total.monthly_total()
        elif choice == "6":
            delete_expense.delete_expense()
        elif choice == "7":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1-7.")

if __name__ == "__main__":
    main()
