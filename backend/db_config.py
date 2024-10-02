import streamlit as st
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def get_db_uri():
    """Construct and return the database URI from Streamlit secrets."""
    db_user = st.secrets["database"]["user"]
    db_password = st.secrets["database"]["password"]
    db_host = st.secrets["database"]["host"]
    db_port = st.secrets["database"]["port"]
    db_name = st.secrets["database"]["name"]

    # Check if all necessary secrets are set
    if not all([db_user, db_password, db_host, db_port, db_name]):
        raise ValueError("One or more database secrets are missing.")
    
    # Construct and return the DATABASE_URL
    return f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Get the database connection URL
DATABASE_URL = get_db_uri()

# Print the database URL for debugging purposes (consider removing in production)
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

# Example usage in a Streamlit app
def main():
    st.title("Database Connection Test")
    try:
        # Test the database connection
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            st.success("Successfully connected to the database!")
    except Exception as e:
        st.error(f"Failed to connect to the database: {str(e)}")

if __name__ == "__main__":
    main()