import mysql.connector
import time
from datetime import datetime

last_checked_id = 0  # Global tracker

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="Vaishnavi Bandil",
        password="*****",
        database="Information"
    )

def check_for_new_data():
    global last_checked_id
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, age, gender FROM People WHERE id > %s ORDER BY id ASC", (last_checked_id,))
    rows = cursor.fetchall()

    if rows:
        print(f"{len(rows)} new record(s) found!")
        for row in rows:
            print(f"ID {row[0]}: {row[1]}, Age: {row[2]}, Gender: {row[3]}")
            # Call your processing logic here (export, ML, etc.)
            last_checked_id = max(last_checked_id, row[0])
    else:
        print("No new records.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    print("Starting DB watcher...")
    while True:
        check_for_new_data()
        time.sleep(5)  # Wait 5 seconds