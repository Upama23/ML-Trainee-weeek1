from fastapi import FastAPI, Depends,HTTPException
from app.database import engine, SessionLocal
from app.database import create_employee_data
from sqlalchemy.orm import Session
from app.models import Base
from app.models import Employee
from app.schemas import EmployeePost,EmployeePostReturn
from sqlalchemy import update
from fastapi import HTTPException

app = FastAPI()

@app.on_event("startup")
async def startup_events():
    Base.metadata.create_all(bind=engine)
    create_employee_data()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/employees")
def get_all_employees(skip: int = 0, limit: int = 10,db: Session = Depends(get_db)):
    employees = db.query(Employee).offset(skip).limit(limit).all()
    print('hi')
    return [EmployeePostReturn(**employee.__dict__) for employee in employees]


@app.get("/employees/{employee_id}")
def get_employee(employee_id: str, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@app.post("/employees",response_model=EmployeePostReturn)
def register_employee(employee: EmployeePost, db: Session = Depends(get_db)):
    db_employee = Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return EmployeePostReturn(**db_employee.__dict__)

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(employee)
    db.commit()
    return {"message": "Employee deleted successfully"}


@app.put("/employees/{employee_id}/{column}/{new_value}", response_model=EmployeePostReturn)
def update_employee_column(employee_id: int, column: str, new_value: str, db: Session = Depends(get_db)):
    allowed_columns = ["name", "department"]  # List of allowed columns to update

    if column not in allowed_columns:
        raise HTTPException(status_code=400, detail="Invalid column name")

    stmt = update(Employee).where(Employee.id == employee_id).values(**{column: new_value})
    updated = db.execute(stmt)

    if updated.rowcount == 0:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.commit()

    # Fetch the updated employee record
    updated_employee = db.query(Employee).filter(Employee.id == employee_id).first()

    return EmployeePostReturn(**updated_employee.__dict__)


@app.get('/')
def root():

    return {"message": "Welcome api"}