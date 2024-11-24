import os
import time
import csv

class DBManager:
    DATABASE_NAME = "binlist-data.csv"
    DATABASE_DIR = "database"
    DATABASE_SOURCE = os.path.join(DATABASE_DIR, DATABASE_NAME)

    def __init__(self, csv_database_source):
        self.csv_database_source = csv_database_source
        self.bin_data = None

    def load_bin_data_from_source(self):
        start_time = time.time()
        self.bin_data = {}
        with open(self.csv_database_source, "r", encoding="utf-8") as db:
            csv_reader = csv.DictReader(db)
            print("CSV database initialization...")
            for row in csv_reader:
                bin_number = row.get("bin")
                bank_brand = row.get("brand")
                if bin_number and bank_brand:
                    self.bin_data[int(bin_number)] = bank_brand
        end_time = time.time()
        elapsed_time = end_time - start_time # DB init timer
        print("CSV database initialized successfully!")
        print(f"Total {len(self.bin_data)} records in {elapsed_time:.2f} seconds.")
        return self.bin_data

    def search_bin_in_data_source(self, bin_number):
        return self.bin_data.get(bin_number)