import os
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db_uri():
    """Construct and return the database URI from environment variables."""
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    # Check if all necessary environment variables are set
    if not all([db_user, db_password, db_host, db_port, db_name]):
        raise ValueError("One or more database environment variables are missing.")
    
    # Construct and return the DATABASE_URL
    return f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Get the database connection URL
DATABASE_URL = get_db_uri()

# Print the database URL for debugging purposes
print(f"Database URL: {DATABASE_URL}")

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()

def get_db():
    """Create a new database session and close it after use."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
