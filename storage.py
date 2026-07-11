import json
import csv

from expense import Expense


def save_expenses(expenses):
    with open('expenses.json', 'w') as outfile:
        expenses_data = []
        for expense in expenses:
            expenses_data.append(expense.to_dict())
        json.dump(expenses_data, outfile, indent=4)

def load_expenses():
    try:
        with open('expenses.json', 'r') as infile:
            expenses_data = json.load(infile)

        expenses = []

        for data in expenses_data:
            expense = Expense.from_dict(data)
            expenses.append(expense)
        return expenses


    except FileNotFoundError:

        print("expenses.json not found.")
        return []


    except json.JSONDecodeError:

        print("expenses.json is corrupted.")
        return []

def export_csv(expenses):
    with open('expenses.csv', 'w', newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Amount",
                         "Category",
                         "Description",
                         "Date"])

        for expense in expenses:
            writer.writerow([expense.amount,
                             expense.category,
                             expense.description,
                             expense.date])


