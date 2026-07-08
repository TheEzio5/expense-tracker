
from expense import Expense
from expense_manager import ExpenseManager

from menu import show_expense_menu

manager = ExpenseManager()


while True:

    show_expense_menu()

    menu_choice = input("Enter your choice: ")
    if menu_choice == "1":



        amount = input("Please enter the amount you want to add: ")
        category = input ("Please enter the category of the expense: ")
        description = input("Please enter the description: ")
        date = input("Please enter the date: ")

        expense = Expense(amount, category, description, date)

        manager.add_expense(expense)



    elif menu_choice == "2":

        manager.show_expenses()

    elif menu_choice == "3":
        print("Thank you for using this program")
        break
    else:
        print("Invalid option.")
