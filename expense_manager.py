

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

