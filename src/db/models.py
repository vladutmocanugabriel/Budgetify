from db.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, Enum as SQLAEnum
from classes.expense_type import ExpenseType


class BudgetCategory(Base):
    __tablename__ = "budget_model"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    starting_total = Column(Float, nullable=False)
    limit = Column(Float, default=0)
    total_spent = Column(Float, default=0)
    remaining_budget = Column(Float, default=0)
    over_budget = Column(Boolean, default=False)

    expenses = relationship("Expense", back_populates="budget_category")

    #user_id = Column(Integer, ForeignKey("users_model.id"))
    #user = relationship("User", back_populates="budgets")

class Expense(Base):
    __tablename__ = "expense_model"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    expense_type = Column(SQLAEnum(ExpenseType), nullable=False)
    
    budget_category_id = Column(Integer, ForeignKey("budget_model.id"), nullable=False)
    budget_category = relationship("BudgetCategory", back_populates="expenses")

    #user_id = Column(Integer, ForeignKey("users_model.id"))
    #user = relationship("User", back_populates="budgets")

#class User(Base):
   # __tablename__ = "users_model"

    #id = Column(Integer, primary_key=True, index=True)
    #username = Column(String, unique=True, index=True, nullable=False)
    #hashed_password = Column(String, nullable=False)

    #budgets = relationship("BudgetCategory", back_populates="user")
    #expenses = relationship("Expense", back_populates="user")
