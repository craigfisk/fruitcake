import os
import psycopg2
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

def test_connection():
    # Retrieve the URL from the environment
    db_url = os.getenv("DATABASE_URL")
    
    try:
        # Establish the connection
        conn = psycopg2.connect(db_url)
        print("Successfully connected to the database!")
        
        # Verify it with a simple query
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        print(f"PostgreSQL version: {db_version[0]}")
        
        cur.close()
        conn.close()
        
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    test_connection()