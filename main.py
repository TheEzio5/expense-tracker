
from expense import Expense
from expense_manager import ExpenseManager
from storage import save_expenses, load_expenses
from datetime import datetime

from menu import show_expense_menu

manager = ExpenseManager()
manager.expenses = load_expenses()


while True:

    show_expense_menu()

    menu_choice = input("Enter your choice: ")
    if menu_choice == "1":


        try:
            amount = int(input("Please enter the amount you want to add: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue
        category = input ("Please enter the category of the expense: ")
        if category.strip() == "":
            print("Category cannot be empty.")
            continue
        description = input("Please enter the description: ")
        if description.strip() == "":
            print("Description cannot be empty.")
            continue
        date = input("Please enter the date (DD-MM-YYYY): ")
        try:
            datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            print("Invalid date format. Use DD-MM-YYYY.")
            continue

        expense = Expense(amount, category, description, date)

        manager.add_expense(expense)
        save_expenses(manager.list_expenses())



    elif menu_choice == "2":

        manager.show_expenses(manager.list_expenses())

    elif menu_choice == "3":
        try:
            expense_index = int(input("Enter expense number: "))
        except ValueError:
            print("Invalid expense number. Please enter a number.")
            continue
        manager.delete_expense(expense_index)
        save_expenses(manager.list_expenses())

    elif menu_choice == "4":
        category = input("Enter expense category: ")
        matched_expenses =  manager.search_expenses(category)
        manager.show_expenses(matched_expenses)

    elif menu_choice == "5":

        manager.statistics_expenses()

    elif menu_choice == "6":
        try:
            expense_index = int(input("Enter expense number: "))
        except ValueError:
            print("Invalid expense number. Please enter a number.")
            continue
        manager.edit_expense(expense_index)
        save_expenses(manager.list_expenses())

    elif menu_choice == "7":
        print("Sort by:")
        print("1. Amount")
        print("2. Category")
        print("3. Date")

        sort_choice = input("Please select your choice: ")

        if sort_choice == "1":
               manager.sort_expenses("amount")

        elif sort_choice == "2":
                manager.sort_expenses("category")

        elif sort_choice == "3":
                manager.sort_expenses("date")

        else:
            print("Invalid option.")
            continue
        manager.show_expenses(manager.list_expenses())


    elif menu_choice == "8":
        print("Thank you for using this program")
        break
    else:
        print("Invalid option.")

