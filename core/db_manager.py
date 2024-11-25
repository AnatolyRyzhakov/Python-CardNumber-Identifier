import os
import time
import csv

class DBManager:
    
    def __init__(self):
        self._DATABASE_NAME: int = "binlist-data.csv"
        self._DATABASE_DIR: int = "database"
        self._DATABASE_SOURCE: int = os.path.join(self._DATABASE_DIR, self._DATABASE_NAME)
        self.bin_data = None

    def get_database_source(self) -> str:
        return self._DATABASE_SOURCE

    def load_bin_data_from_source(self) -> dict:
        start_time = time.time()
        self.bin_data = {}
        with open(self._DATABASE_SOURCE, "r", encoding="utf-8") as db:
            csv_reader = csv.DictReader(db)
            print("CSV database initialization...")
            for row in csv_reader:
                bin_number = row.get("bin")
                bank_issuer = row.get("issuer")
                if bin_number and bank_issuer:
                    self.bin_data[int(bin_number)] = bank_issuer
        end_time = time.time()
        elapsed_time = end_time - start_time # DB init timer
        print("CSV database initialized successfully!")
        print(f"Total {len(self.bin_data)} records in {elapsed_time:.2f} seconds.")
        return self.bin_data

    def search_bin_in_data_source(self, bin_number: int) -> str:
        bank_issuer = self.bin_data.get(bin_number)
        if bank_issuer:
            return bank_issuer
        elif bank_issuer is None:
            return "Unknown bank"