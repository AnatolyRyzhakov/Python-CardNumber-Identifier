from flask import Flask
from core.db_manager import load_bin_data_from_source, DATABASE_SOURCE

app: Flask = Flask(__name__)
bin_data = load_bin_data_from_source(DATABASE_SOURCE)

from routes.routes import *

if __name__ == ("__main__"):
    if bin_data:
        app.run(debug=True)