from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.models import BudgetCategory, Expense
from api.schemas import BudgetCreate, BudgetOut, ExpenseCreate, ExpenseOut
from fastapi import HTTPException

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#POST /budgets - Create Budget
@router.post("/budgets", response_model=BudgetOut)
def create_budget(budget:BudgetCreate, db:Session = Depends(get_db)):
    new_budget = BudgetCategory(
        name=budget.name,
        starting_total=budget.starting_total,
        limit=0,
        total_spent=0,
        over_budget=False
    )
    db.add(new_budget)
    db.commit()
    db.refresh(new_budget)
    return new_budget


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

#POST /{budget_id}/expenses - Create expense
@router.post("/{budget_id}/expenses", response_model=ExpenseOut)
def create_expense(budget_id: int, expense:ExpenseCreate, db:Session = Depends(get_db)):
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
    for e in budget.expenses:
        if e.id == expense_id:
            expense = e
            break

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    return expense