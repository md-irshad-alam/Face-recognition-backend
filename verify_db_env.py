import database
import os
from dotenv import load_dotenv

load_dotenv()

print(f"DB_HOST: {os.getenv('DB_HOST')}")
print(f"DB_NAME: {os.getenv('DB_NAME')}")
print(f"DB_USER: {os.getenv('DB_USER')}")
# Do not print password

try:
    conn = database.create_connection()
    if conn and conn.is_connected():
        print("Successfully connected to the database!")
        conn.close()
    else:
        print("Failed to connect to the database.")
except Exception as e:
    print(f"An error occurred: {e}")
