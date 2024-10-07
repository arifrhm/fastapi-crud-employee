# app/database.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database configuration from environment variables
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:"
    + f"{POSTGRES_PASSWORD}"
    + "@"
    + f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

print(SQLALCHEMY_DATABASE_URL)

# Configure the connection pool for optimal CPU and RAM usage
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # Number of connections to maintain in the pool
    pool_size=10,
    # Allow 5 extra connections during heavy load
    max_overflow=5,
    # Wait 30 seconds before raising connection timeout error
    pool_timeout=30,
    # Recycle connections every 30 minutes (1800 seconds)
    pool_recycle=1800,
    # Check if connection is alive before using it
    pool_pre_ping=True,
)

# Session and Base configuration
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)
Base = declarative_base()
