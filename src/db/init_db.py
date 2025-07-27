from db.models import BudgetCategory, Expense
from db.database import Base, engine

Base.metadata.create_all(bind=engine)
