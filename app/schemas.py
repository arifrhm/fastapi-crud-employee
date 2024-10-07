from pydantic import BaseModel, ConfigDict


class EmployeeBase(BaseModel):
    name: str
    position: str
    salary: int


class EmployeeCreate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True  # Use from_attributes instead of orm_mode
    )
