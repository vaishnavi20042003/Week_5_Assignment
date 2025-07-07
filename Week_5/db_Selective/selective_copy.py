import mysql.connector

SOURCE_DB = "Information"
DEST_DB = "Information_Lite"

DB_CONFIG = {
    "host": "localhost",
    "user": "Vaishnavi Bandil",
    "password": "*****"
}

SELECTIVE_TABLES = {
    "People": ["name", "age"],
}

def connect():
    return mysql.connector.connect(**DB_CONFIG)

def create_destination_db(cursor):
    cursor.execute(f"DROP DATABASE IF EXISTS {DEST_DB}")
    cursor.execute(f"CREATE DATABASE {DEST_DB}")
    print(f"Created destination database: {DEST_DB}")

def create_table_structure(src_cursor, dest_cursor, table, columns):
    cols_def = []

    for col in columns:
        src_cursor.execute(f"""
            SELECT COLUMN_NAME, COLUMN_TYPE
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s AND COLUMN_NAME = %s
        """, (SOURCE_DB, table, col))
        result = src_cursor.fetchone()

        if result:
            col_name, col_type = result
            cols_def.append(f"`{col_name}` {col_type}")
        else:
            print(f"Column '{col}' not found in table '{table}'")

    if not cols_def:
        print(f"Skipping table {table} - No valid columns found.")
        return

    create_stmt = f"CREATE TABLE {DEST_DB}.{table} ({', '.join(cols_def)})"
    dest_cursor.execute(create_stmt)
    print(f"Created table {table} with columns: {columns}")

def copy_data(src_cursor, dest_cursor, table, columns):
    col_str = ", ".join(columns)
    src_cursor.execute(f"SELECT {col_str} FROM {SOURCE_DB}.{table}")
    rows = src_cursor.fetchall()

    if rows:
        placeholders = ", ".join(["%s"] * len(columns))
        insert_query = f"INSERT INTO {DEST_DB}.{table} ({col_str}) VALUES ({placeholders})"
        dest_cursor.executemany(insert_query, rows)
        print(f"Copied {len(rows)} rows to {table}")
    else:
        print(f"No data found in {table}")


def main():
    conn = connect()
    src_cursor = conn.cursor()
    dest_cursor = conn.cursor()

    create_destination_db(dest_cursor)

    for table, columns in SELECTIVE_TABLES.items():
        create_table_structure(src_cursor, dest_cursor, table, columns)
        copy_data(src_cursor, dest_cursor, table, columns)

    conn.commit()
    src_cursor.close()
    dest_cursor.close()
    conn.close()
    print("Selective data migration completed successfully.")

if __name__ == "__main__":
    main()