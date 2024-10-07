from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud
from app import models
from app import schemas
from app.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/employees", response_model=list[schemas.Employee])
def read_employees(skip: int = 0,
                   limit: int = 10,
                   db: Session = Depends(get_db)):
    employees = crud.get_employees(db, skip=skip, limit=limit)
    return employees


@app.get("/employees/{id}", response_model=schemas.Employee)
def read_employee(id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, employee_id=id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@app.post("/employees", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate,
                    db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)


@app.put("/employees/{id}", response_model=schemas.Employee)
def update_employee(
    id: int, employee: schemas.EmployeeCreate, db: Session = Depends(get_db)
):
    updated_employee = crud.update_employee(db=db,
                                            employee_id=id,
                                            employee=employee)
    if updated_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_employee


@app.delete("/employees/{id}", response_model=schemas.Employee)
def delete_employee(id: int, db: Session = Depends(get_db)):
    deleted_employee = crud.delete_employee(db=db, employee_id=id)
    if deleted_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return deleted_employee
