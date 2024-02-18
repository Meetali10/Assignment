class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, date):
        expense = {
            'amount': amount,
            'category': category,
            'date': date
        }
        self.expenses.append(expense)

    def get_expenses_by_category(self):
        expenses_by_category = {}
        for expense in self.expenses:
            category = expense['category']
            if category not in expenses_by_category:
                expenses_by_category[category] = []
            expenses_by_category[category].append(expense)
        return expenses_by_category
