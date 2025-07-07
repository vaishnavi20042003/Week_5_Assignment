import pandas as pd
from sqlalchemy import create_engine
from fastavro import writer, parse_schema
import os

# MySQL connection details
host = "localhost"
port = 3306
user = "Vaishnavi Bandil"
password = "*****"
database = "Information"
table = "People"

# Create connection string
conn_str = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(conn_str)

# Read data from table
df = pd.read_sql(f"SELECT * FROM {table}", con=engine)

# Export directory
os.makedirs("output", exist_ok=True)

# Export to CSV
df.to_csv("output/users.csv", index=False)

# Export to Parquet
df.to_parquet("output/users.parquet", engine="pyarrow", index=False)

# Export to Avro
schema = {
    "doc": "User Data",
    "name": "User",
    "namespace": "example.avro",
    "type": "record",
    "fields": [
        {"name": col, "type": "string"} for col in df.columns
    ]
}

records = df.astype(str).to_dict(orient="records")

with open("output/users.avro", "wb") as out:
    writer(out, parse_schema(schema), records)

print("Export complete. Files saved in 'output' folder.")