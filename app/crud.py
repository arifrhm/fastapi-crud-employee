from sqlalchemy.orm import Session
from app import models
from app import schemas


def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).\
        filter(models.Employee.id == employee_id).first()


def get_employees(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Employee).offset(skip).limit(limit).all()


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    # Use model_dump if needed
    db_employee = models.Employee(**employee.model_dump())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def update_employee(db: Session,
                    employee_id: int,
                    employee: schemas.EmployeeCreate):
    db_employee = get_employee(db, employee_id)
    if db_employee:
        for (
            key,
            value,
        ) in employee.model_dump().items():  # Use model_dump instead of dict()
            setattr(db_employee, key, value)
        db.commit()
        db.refresh(db_employee)
        return db_employee
    return None


def delete_employee(db: Session, employee_id: int):
    db_employee = get_employee(db, employee_id)
    if db_employee:
        db.delete(db_employee)
        db.commit()
        return db_employee
    return None
