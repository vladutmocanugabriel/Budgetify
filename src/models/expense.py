from enum import Enum

class ExpenseType(Enum):
    FOOD = "FOOD"
    CAR_GAS = "CAR_GAS"
    CIGGARETES = "CIGGARETES"
    SUBSCRIPTIONS = "SUBSCRIPTIONS"
    CLOTHES = "CLOTHES"
    TAKE_OUT = "TAKE_OUT"
    GOING_OUT = "GOING_OUT"
    SPORT = "SPORT"
    GIFTS = "GIFTS"
    MISSCELANEOUS = "MISSCELANEOUS"

class Expense:
    def __init__(self, name, amount, expense_type: ExpenseType):
        self.name = name
        self.amount = amount
        self.expense_type = expense_type

    def __repr__(self):
        return f"Expense(name='{self.name}', amount={self.amount}, type={self.expense_type.name})"


