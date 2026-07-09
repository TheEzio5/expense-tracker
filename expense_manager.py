

from expense import Expense


class ExpenseManager:

    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)



    def list_expenses(self):
            return self.expenses

    def show_expenses(self,expenses):

        if not expenses:
            print("No expenses found")
        else:

            for index, expense in enumerate(expenses, start=1):

                print("-" * 10)
                print(f"Expense #{index}")
                print(f"Amount: {expense.amount}€")
                print(f"Category: {expense.category}")
                print(f"Description: {expense.description}")
                print(f"Date: {expense.date}")
                print("-" * 10)

    def delete_expense(self, expense_index):
        if 1 <= expense_index <= len(self.expenses):
            self.expenses.pop(expense_index - 1)
            print("Deleted expense.")
        else:
            print("Expense number out of range.")

    def search_expenses(self, expenses_category):
        matched_expenses = []
        for expense in self.expenses:

            if expense.category.lower() == expenses_category.lower():
                matched_expenses.append(expense)
        return matched_expenses

    def statistics_expenses(self):

        if not self.expenses:
            print("No expenses found.")
            return

        total_expenses = len(self.expenses)
        print(f"Total expenses: {total_expenses}")

        total_spent_expenses = 0
        for expense in self.expenses:
            total_spent_expenses += expense.amount
        print(f"Total spent expenses: {total_spent_expenses}€")

        if total_expenses == 0:
            print("Error cannot divide by 0")
        else:
            average_spent_expenses = total_spent_expenses / total_expenses

            print(f"Average spent expenses: {average_spent_expenses}€")

        max_expense = max(self.expenses, key=lambda expense: expense.amount)
        print(f"Maximum spent expenses: {max_expense.amount}€")

        min_expense = min(self.expenses, key=lambda expense: expense.amount)
        print(f"Minimum spent expenses: {min_expense.amount}€")

    def edit_expense(self,expense_index):
        if not self.expenses:
            print("No expenses found.")
            return
        if 1 <= expense_index <= len(self.expenses):

            expense = self.expenses[expense_index - 1]
            new_amount = input(f"Enter new amount: ({expense.amount}): ")
            if new_amount != "":
                expense.amount = int(new_amount)

            new_category = input(f"Enter new category ({expense.category}): ")
            if new_category != "":
                expense.category = new_category
            new_description = input(f"Enter new description: ({expense.description}): ")
            if new_description != "":
                expense.description = new_description
            new_date = input(f"Enter new date: ({expense.date}): ")
            if new_date != "":
                expense.date = new_date
        else:
            print("Expense number out of range.")






