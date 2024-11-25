from flask import Flask
from core.db_manager import DBManager as DBM

# SRS-1
# EN: The program loads a BIN number database from a CSV file on the disk at startup
# RU: При запуске программа считывает из csv-файла на диске базу данных BIN-номеров
db: DBM = DBM()
db.load_bin_data_from_source()

app: Flask = Flask(__name__)

from routes.routes import *

if __name__ == ("__main__"):
    # SRS-2
    # EN: After successful loading, the application becomes an HTTP server
    # RU: После успешной загрузки приложение «превращается» в HTTP-сервер
    if len(db.bin_data) > 0:
        app.run(debug=False)