import mysql.connector

SOURCE_DB = "Information"
DEST_DB = "Information_Copy"

DB_CONFIG = {
    "host": "localhost",
    "user": "Vaishnavi Bandil",
    "password": "*****",
}

def connect():
    return mysql.connector.connect(**DB_CONFIG)

def create_destination_db(cursor):
    cursor.execute(f"DROP DATABASE IF EXISTS {DEST_DB}")
    cursor.execute(f"CREATE DATABASE {DEST_DB}")
    print(f"Created destination database: {DEST_DB}")

def get_table_names(cursor):
    cursor.execute(f"SHOW TABLES FROM {SOURCE_DB}")
    return [row[0] for row in cursor.fetchall()]

def copy_table_structure(cursor, table):
    cursor.execute(f"SHOW CREATE TABLE {SOURCE_DB}.{table}")
    create_stmt = cursor.fetchone()[1]
    cursor.execute(f"USE {DEST_DB}")
    cursor.execute(create_stmt)
    print(f"Table structure copied: {table}")

def copy_table_data(src_cursor, dest_cursor, table):
    src_cursor.execute(f"SELECT * FROM {SOURCE_DB}.{table}")
    rows = src_cursor.fetchall()

    if rows:
        cols = [desc[0] for desc in src_cursor.description]
        col_str = ", ".join(cols)
        placeholders = ", ".join(["%s"] * len(cols))
        insert_query = f"INSERT INTO {DEST_DB}.{table} ({col_str}) VALUES ({placeholders})"
        dest_cursor.executemany(insert_query, rows)
        print(f"Data copied: {table} → {len(rows)} rows")
    else:
        print(f"No data to copy in: {table}")

def main():
    conn = connect()
    src_cursor = conn.cursor()
    dest_cursor = conn.cursor()

    print("Cloning all tables...")
    create_destination_db(dest_cursor)
    tables = get_table_names(src_cursor)
    print(f"Found tables: {tables}")

    for table in tables:
        copy_table_structure(dest_cursor, table)
        copy_table_data(src_cursor, dest_cursor, table)

    conn.commit()
    src_cursor.close()
    dest_cursor.close()
    conn.close()
    print(f"Database cloned successfully: {SOURCE_DB} → {DEST_DB}")

if __name__ == "__main__":
    main()