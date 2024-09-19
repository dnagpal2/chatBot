from sqlalchemy.orm import Session
from sqlalchemy import text

def test_db_connection():
    try:
        with Session(engine) as session:
            session.execute(text("SELECT 1"))
            print("Database connection successful!")
    except Exception as e:
        print(f"Database connection failed: {e}")

# Call this function to test
test_db_connection()