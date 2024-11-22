import os
import time
import csv

DATABASE_NAME = "binlist-data.csv"
DATABASE_DIR = "database"
DATABASE_SOURCE = os.path.join(DATABASE_DIR, DATABASE_NAME)

def load_bin_data_from_source(csv_database_source):
    start_time = time.time()
    bin_data = {}
    with open(csv_database_source, "r", encoding="utf-8") as db:
        csv_reader = csv.DictReader(db)
        print("CSV database initialization...")
        for row in csv_reader:
            bin_number = row.get("bin")
            bank_brand = row.get("brand")
            if bin_number and bank_brand:
                bin_data[int(bin_number)] = bank_brand
    end_time = time.time()
    elapsed_time = end_time - start_time # DB init timer
    print("CSV database initialized successfully!")
    print(f"Total {len(bin_data)} records in {elapsed_time:.2f} seconds.")
    return bin_data

def search_bin_in_data_source(bin_number, bin_data):
    return bin_data.get(bin_number)