from classes.expense import Expense

class BudgetCategory:
    def __init__(self, name, starting_total):
        self.name = name
        self.starting_total = starting_total
        self.limit = 0
        self.total_spent = 0
        self.remaining_budget = 0
        self.over_budget = False
        self.expenses = []

    def __repr__(self):
        return f"BudgetCategory(name='{self.name}', starting={self.starting_total}, spent={self.total_spent}, over_budget={self.over_budget})"

    #SET and CHECK budget
    def set_limit(self, amount):
        self.limit = amount
        return self.limit

    def get_remaining(self):
        self.remaining_budget =  self.starting_total - self.total_spent
        return self.remaining_budget
    
    def add_to_expenses_list(self, expense):
        return self.expenses.append(expense)
    
    def remove_expense_from_list(self, expense):
        return self.expenses.remove(expense)
    
    def is_over_budget(self):
        if self.get_remaining() < self.limit:
            self.over_budget = True
        elif self.get_remaining() == self.limit:
            self.over_budget = False
        else:
            self.over_budget = False
        return self.over_budget
    
    #UPDATE and CALCULATE Budget
    def add_expense(self, name, amount, type):
        expense = Expense(name, amount, type)
        self.total_spent += expense.amount
        self.remaining_budget = self.get_remaining()
        self.add_to_expenses_list(expense)
    
    def remove_expense(self, expense):
        self.total_spent -= expense.amount
        self.remove_expense_from_list(expense)
    
    def get_total_spent(self):
        return self.total_spent
    
    #?????
    def add_funds(self, amount):
        self.re -= amount
        return self.total_spent


        