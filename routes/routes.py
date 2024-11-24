from app import app, db
from flask import render_template, request
import time

@app.route("/", methods=["GET"])
def index():
        # SRS-3
        # EN: Any request took at least 3 seconds to complete
        # RU: Чтобы любой запрос выполнялся сравнительно медленно (не менее трех секунд)
        time.sleep(3)
        return render_template("index.html")

# SRS-6
# EN: The browser should display either the bank information or an error message, depending on the request result
# RU: В результате выполнения запроса в браузере должна быть отображена страница либо с найденной информацией о банке, либо с сообщением об ошибке.
@app.route("/identify", methods=["GET"])
def return_bank_brand_via_bin():
    bin_number = request.args.get("BIN")
    if int(bin_number) > 0:
        bank_brand_name = db.search_bin_in_data_source(int(bin_number))
        result = f"For BIN {bin_number} bank brand name is: {bank_brand_name}"
        time.sleep(3)
        return result
    else:
        result = f"Invalid BIN!"
        time.sleep(3)
        return result
