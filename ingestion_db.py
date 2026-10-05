import os
import time
import logging
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from urllib.parse import quote_plus

os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

load_dotenv()
db_password = os.getenv('DB_PASSWORD')
safe_password = quote_plus(db_password) if db_password else ""

db_url = f'postgresql://postgres:{safe_password}@localhost:5432/inventory_db'
engine = create_engine(db_url)


def ingest_db(file_path, table_name, engine, chunksize=50000):
    first_chunk = True
    batch_num = 1
    
    for chunk in pd.read_csv(file_path, chunksize=chunksize):
        if_exists_mode = 'replace' if first_chunk else 'append'
        chunk.to_sql(table_name, con=engine, if_exists=if_exists_mode, index=False, method='multi')
        logging.info(f"  -> Batch {batch_num} uploaded ({len(chunk)} rows)")
        first_chunk = False
        batch_num += 1


def load_raw_data():
    start = time.time()
    data_dir = 'data'
    
    for file in os.listdir(data_dir):
        if file.endswith('.csv'):
            file_path = os.path.join(data_dir, file)
            table_name = file.replace('.csv', '')
            
            print(f"Uploading '{table_name}' into PostgreSQL...")
            logging.info(f'Ingesting {file} into table: {table_name}')
            
            ingest_db(file_path, table_name, engine)
            print(f"Table '{table_name}' loaded successfully!\n")
            
    end = time.time()
    total_time = (end - start) / 60
    
    logging.info('-------------------Ingestion Complete-------------------')
    logging.info(f'Total Time Taken: {total_time:.2f} minutes')
    print(f"Data Ingestion Successful! Total time taken: {total_time:.2f} minutes")


if __name__ == '__main__':

    load_raw_data()

    print("\n--- PostgreSQL Tables Verification ---")
    tables = ['begin_inventory', 'end_inventory', 'purchase_prices', 'purchases', 'sales', 'vendor_invoice']

    for t in tables:
        count = pd.read_sql(f'SELECT COUNT(*) FROM {t};', engine).iloc[0, 0]
        print(f"✓ Table '{t}': {count:,} total rows")

    df_begin = pd.read_sql("SELECT * FROM begin_inventory LIMIT 10000;", engine)
    df_sales = pd.read_sql("SELECT * FROM sales LIMIT 10000;", engine)

    print("\n--- Begin Inventory Preview ---")
    print(df_begin.head())

    print("\n--- Begin Inventory Null Values ---")
    print(df_begin.isnull().sum())

    print("\n--- Sales Table Info ---")
    print(df_sales.info())

    engine.dispose()
