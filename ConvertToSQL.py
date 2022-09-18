import gzip
import os
import shutil
import sqlite3
from glob import glob

import pandas as pd

# unziping files:
with gzip.open("calendar.csv.gz", "rb") as f_in:
    with open("calendar.csv", "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

with gzip.open("listings.csv.gz", "rb") as f_in:
    with open("listings.csv", "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

with gzip.open("reviews.csv.gz", "rb") as f_in:
    with open("reviews.csv", "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

# Useful variables
source_files = "./*.csv"  # All CSVs in current folder
destination_file = "amsterdam-airbnb.db"  # SQLite DB file

# Create SQLite connection and file at the same time
with sqlite3.connect(destination_file) as con:
    # Traverse all CSV files
    for csv_file in glob(source_files):
        # Use pandas for reading
        df = pd.read_csv(csv_file)
        # Get filename
        file_name, file_ext = os.path.splitext(os.path.basename(csv_file))
        print(f"Processing {file_name}...")
        # Create or replace the table
        df.to_sql(file_name, con, if_exists="replace", index=False)

print("Done")

"""
import glob
import os

import pandas as pd
from sqlalchemy import create_engine

for file in glob.glob("*.csv"):
    df = pd.read_csv(file)

    # Create SQLAlchemy engine to connect to MySQL Database
    engine = create_engine("mysql+mysqldb://root:<PASSWORD>@127.0.0.1/amsterdam-airbnb")

    # Convert dataframe to sql table
    df.to_sql(file[:-4], engine, index=False)

    print("done")
"""
