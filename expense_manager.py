from selectors import SelectSelector

from expense import Expense


class ExpenseManager:

    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)



    def list_expenses(self):
            return self.expenses

    def show_expenses(self):

        if not self.expenses:
            print("No expenses found")
        else:

            for expense in self.expenses:


                print("-" * 10)
                print(f"Amount: {expense.amount}€")
                print(f"Category: {expense.category}")
                print(f"Description: {expense.description}")
                print(f"Date: {expense.date}")
                print("-" * 10)

