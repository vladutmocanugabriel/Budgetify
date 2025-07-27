from pydantic import BaseModel
from classes.expense_type import ExpenseType

class BudgetCreate(BaseModel):
    name: str
    starting_total: float
class BudgetOut(BaseModel):
    id: int
    name: str
    starting_total: float

    limit: float
    total_spent: float
    over_budget: bool
    class Config:
        orm_mode = True

class ExpenseCreate(BaseModel):
    name: str
    amount: float
    expense_type: ExpenseType
class ExpenseOut(BaseModel):
    id: int
    name: str
    amount: float
    expense_type: ExpenseType
    budget_category_id: int
    class Config:
        orm_mode = True


