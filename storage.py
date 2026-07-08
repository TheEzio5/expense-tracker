import json

from expense import Expense


def save_expenses(expenses):
    with open('expenses.json', 'w') as outfile:
        expenses_data = []
        for expense in expenses:
            expenses_data.append(expense.to_dict())
        json.dump(expenses_data, outfile, indent=4)

def load_expenses():
    with open('expenses.json', 'r') as infile:
        expenses_data = json.load(infile)

        expenses = []

        for data in expenses_data:
            expense = Expense.from_dict(data)
            expenses.append(expense)
        return expenses