# Employee Management API

## Overview
The **Employee Management API** is a RESTful API designed for managing employee data, built using **FastAPI** and **SQLAlchemy**. It provides endpoints to create, read, update, and delete employee records in a **PostgreSQL** database.

## Features
- **CRUD Operations**: Full functionality to Create, Read, Update, and Delete employee records.
- **Database Integration**: Utilizes SQLAlchemy ORM for seamless database interactions.
- **Environment Configuration**: Leverages environment variables for database configuration to enhance security and flexibility.
- **Dependency Management**: Manages packages using `pip`.

## Project Structure
```
.
├── Dockerfile
├── README.md
├── app
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── build_test_run.sh
├── clear_cache.sh
├── configmap.yaml
├── deployment.yaml
├── docker-compose.yml
├── init.sql
├── req.txt
├── service.yaml
└── tests
    ├── __init__.py
    └── test_main.py
```

## Prerequisites
Before you begin, ensure you have the following installed:
- **Docker** and **Docker Compose**
- **Kubernetes** (with kubectl)
- **Python 3.10+** (for local development)
- **PostgreSQL** database (for local testing)

## Installation

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Set Up Environment Variables
1. **Copy the Example Environment File**:
   ```bash
   cp .env.example .env
   ```

2. **Edit the `.env` File**:
   Open the `.env` file in a text editor and set the following variables:
   ```plaintext
   POSTGRES_USER=<your_postgres_user>
   POSTGRES_PASSWORD=<your_postgres_password>
   POSTGRES_DB=<your_database_name>
   POSTGRES_HOST=<your_database_host>
   POSTGRES_PORT=<your_database_port>
   ```

### Step 3: Build and Run the Application using Docker

1. **Make the build_test_run.sh Script Executable**:
   ```bash
   chmod +x build_test_run.sh
   ```

2. **Run the Script**:
   This script will build the Docker image, run tests, and start the FastAPI server.
   ```bash
   ./build_test_run.sh
   ```

3. **Access the API Documentation**:
   Open your browser and navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to view the interactive API documentation.


## Kubernetes Deployment

### Step 1: Create Kubernetes Resources

1. **Apply the ConfigMap**:
   ```bash
   kubectl apply -f configmap.yaml
   ```

2. **Deploy the Application**:
   ```bash
   kubectl apply -f deployment.yaml
   ```

3. **Expose the Service**:
   ```bash
   kubectl apply -f service.yaml
   ```

### Step 2: Access the API in Kubernetes

- **Get the External IP or NodePort**:
  Use the following command to retrieve the service details:
  ```bash
  kubectl get services
  ```

- **Access the API Documentation**:
  Navigate to the external IP or NodePort that is displayed to access the API documentation at `/docs`.

## Clear Cache
If you need to clear Python bytecode caches or pytest cache, you can run:
```bash
./clear_cache.sh
```