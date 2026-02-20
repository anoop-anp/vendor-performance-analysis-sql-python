import pandas as pd
import os
from sqlalchemy import create_engine
import time
import logging

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

engine = create_engine("sqlite:///inventory.db")


def ingest_db_in_chunks(file_path, table_name, engine, chunksize=100_000):
    first_chunk = True

    for chunk in pd.read_csv(file_path, chunksize=chunksize):
        chunk.to_sql(
            table_name,
            con=engine,
            if_exists="replace" if first_chunk else "append",
            index=False
        )
        first_chunk = False


def load_raw_data():
    start = time.time()

    for file in os.listdir("data"):
        if file.endswith(".csv"):
            file_path = os.path.join("data", file)
            table_name = file[:-4]

            logging.info(f"Starting ingestion for {file}")
            ingest_db_in_chunks(file_path, table_name, engine)
            logging.info(f"Completed ingestion for {file}")

    total_time = (time.time() - start) / 60
    logging.info(f"Ingestion Complete. Total Time: {total_time:.2f} minutes")


if __name__ == "__main__":
    load_raw_data()