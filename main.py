
from expense import Expense
from expense_manager import ExpenseManager
from storage import save_expenses, load_expenses


from menu import show_expense_menu

manager = ExpenseManager()
manager.expenses = load_expenses()


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
        save_expenses(manager.list_expenses())



    elif menu_choice == "2":

        manager.show_expenses(manager.list_expenses())

    elif menu_choice == "3":
        expense_index = int(input("Enter expense number: "))
        manager.delete_expense(expense_index)
        save_expenses(manager.list_expenses())

    elif menu_choice == "4":
        category = input("Enter expense category: ")
        matched_expenses =  manager.search_expenses(category)
        manager.show_expenses(matched_expenses)

    elif menu_choice == "5":
        print("Thank you for using this program")
        break
    else:
        print("Invalid option.")
