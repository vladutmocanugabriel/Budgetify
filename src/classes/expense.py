from expense_type import ExpenseType

class Expense:
    def __init__(self, name, amount, expense_type: ExpenseType):
        self.name = name
        self.amount = amount
        self.expense_type = expense_type

    def __repr__(self):
        return f"Expense(name='{self.name}', amount={self.amount}, type={self.expense_type.name})"


