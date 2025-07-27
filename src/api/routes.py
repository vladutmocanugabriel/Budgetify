from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.models import BudgetCategory, Expense
from api.schemas import BudgetCreate, BudgetOut, ExpenseCreate, ExpenseOut, BudgetLimitUpdate
from fastapi import HTTPException
from classes.budget import BudgetCategory as BudgetLogic
from classes.expense import Expense as ExpenseLogic

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#################  BUDGETS  ###########################################################################

#POST /budgets - Create Budget
@router.post("/budgets", response_model=BudgetOut)
def create_budget(budget:BudgetCreate, db:Session = Depends(get_db)):
    new_budget = BudgetCategory(
        name=budget.name,
        starting_total=budget.starting_total,
        limit=0,
        total_spent=0,
        remaining_budget=0,
        over_budget=False
    )
    db.add(new_budget)
    db.commit()
    db.refresh(new_budget)
    return new_budget

#PATCH /budgets/{budget_id}/limit - Update the budget's limit
@router.patch("/budgets/{budget_id}/limit", response_model=BudgetOut)
def update_budget_limit(budget_id: int, update:BudgetLimitUpdate, db:Session = Depends(get_db)):
    budget = db.query(BudgetCategory).filter(BudgetCategory.id == budget_id).first()
    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")
    
    logic = BudgetLogic(budget.name, budget.starting_total)
    logic.limit = budget.limit
    logic.total_spent = budget.total_spent

    logic.set_limit(update.limit)
    budget.limit = logic.limit

    budget.over_budget = logic.is_over_budget()

    db.commit()
    db.refresh(budget)
    return budget


#GET /budgets/{id} - Get Budget
@router.get("/budgets/{budget_id}", response_model=BudgetOut)
def get_budget_by_id(budget_id: int, db: Session = Depends(get_db)):
    budget = db.query(BudgetCategory).filter(BudgetCategory.id == budget_id).first()
    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")

    return budget


#GET /budgets - Get All Budgets
@router.get("/budgets", response_model=List[BudgetOut])
def get_all_budgets(db:Session = Depends(get_db)):
    return db.query(BudgetCategory).all()


#################  EXPENSES  ###########################################################################

#POST /{budget_id}/expenses - Create expense
@router.post("/{budget_id}/expenses", response_model=ExpenseOut)
def create_expense(budget_id: int, expense:ExpenseCreate, db:Session = Depends(get_db)):
    budget = db.query(BudgetCategory).filter(BudgetCategory.id == budget_id).first()
    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")
    
    logic = BudgetLogic(budget.name, budget.starting_total)
    logic.limit = budget.limit
    logic.remaining_budget = budget.remaining_budget
    logic.total_spent = budget.total_spent

    logic.add_expense(expense.name, expense.amount, expense.expense_type)
    budget.total_spent = logic.total_spent
    budget.remaining_budget = logic.remaining_budget
    budget.over_budget = logic.is_over_budget()

    new_expense = Expense(
        name = expense.name,
        amount = expense.amount,
        expense_type = expense.expense_type,
        budget_category_id = budget_id
    )
    
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

#GET /expenses - Get all Expenses for a Budget
@router.get("/expenses/{budget_id}", response_model = List[ExpenseOut])
def get_all_expenses_for_budget(budget_id: int, db:Session = Depends(get_db)):
    budget = db.query(BudgetCategory).filter(BudgetCategory.id == budget_id).first()
    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")

    return budget.expenses

#GET /expenses/{budget_id}/{expense_id} - Get Expense from a budget
@router.get("/expenses/{budget_id}/{expense_id}", response_model=ExpenseOut)
def get_expense_from_budget_by_id(budget_id: int, expense_id: int, db: Session = Depends(get_db)):
    budget = db.query(BudgetCategory).filter(BudgetCategory.id == budget_id).first()
    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")
    
    expense = None
    for elem in budget.expenses:
        if elem.id == expense_id:
            expense = elem
            break

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    return expense