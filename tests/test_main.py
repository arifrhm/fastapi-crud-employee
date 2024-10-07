import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app, get_db
from app.database import Base

# In-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False,
                                   autoflush=False,
                                   bind=engine)


# Override get_db to use test database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


# Apply the override
app.dependency_overrides[get_db] = override_get_db

# Set up the test client
client = TestClient(app)

# Create the test database schema
Base.metadata.create_all(bind=engine)


@pytest.fixture
def test_employee_data():
    return {"name": "John Doe",
            "position": "Software Engineer",
            "salary": 60000}


def test_create_employee(test_employee_data):
    response = client.post("/employees", json=test_employee_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == test_employee_data["name"]
    assert data["position"] == test_employee_data["position"]
    assert data["salary"] == test_employee_data["salary"]
    assert "id" in data


def test_read_employees():
    response = client.get("/employees")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_read_employee(test_employee_data):
    # Create employee first
    response = client.post("/employees", json=test_employee_data)
    employee_id = response.json()["id"]

    # Test read employee
    response = client.get(f"/employees/{employee_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == employee_id
    assert data["name"] == test_employee_data["name"]


def test_update_employee(test_employee_data):
    # Create employee first
    response = client.post("/employees", json=test_employee_data)
    employee_id = response.json()["id"]

    updated_data = {"name": "Jane Doe",
                    "position": "Senior Engineer",
                    "salary": 80000}

    # Test update employee
    response = client.put(f"/employees/{employee_id}", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == updated_data["name"]
    assert data["position"] == updated_data["position"]
    assert data["salary"] == updated_data["salary"]


def test_delete_employee(test_employee_data):
    # Create employee first
    response = client.post("/employees", json=test_employee_data)
    employee_id = response.json()["id"]

    # Test delete employee
    response = client.delete(f"/employees/{employee_id}")
    assert response.status_code == 200

    # Test read the deleted employee
    response = client.get(f"/employees/{employee_id}")
    assert response.status_code == 404
