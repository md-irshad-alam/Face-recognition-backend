import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

try:
    # Connect without database to list available ones
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', '')
    )
    cursor = conn.cursor()
    cursor.execute("SHOW DATABASES")
    for db in cursor:
        print(db)
    conn.close()
except Exception as e:
    print(f"Error: {e}")
