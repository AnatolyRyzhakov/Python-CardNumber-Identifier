from app import app, db
from flask import render_template, request
import time

# SRS-3
# EN: Any request took at least 3 seconds to complete
# RU: Чтобы любой запрос выполнялся сравнительно медленно (не менее трех секунд)
CUSTOM_SLEEP_WAITER: int = 3

@app.route("/", methods=["GET"])
def index() -> str:
        time.sleep(CUSTOM_SLEEP_WAITER)
        return render_template("index.html")

# SRS-6
# EN: The browser should display either the bank information or an error message, depending on the request result
# RU: В результате выполнения запроса в браузере должна быть отображена страница либо с найденной информацией о банке, либо с сообщением об ошибке.
@app.route("/identify", methods=["GET"])
def return_bank_issuer_via_bin() -> str:
    bin_number = request.args.get("BIN")
    try:
        if int(bin_number) > 0:
            bank_issuer_name = db.search_bin_in_data_source(int(bin_number))
            result = f"Identify BIN {bin_number}: {bank_issuer_name}"
            time.sleep(CUSTOM_SLEEP_WAITER)
            return result
        elif bin_number.isdigit() or int(bin_number) <= 0:
            result = f"Invalid BIN!"
            time.sleep(CUSTOM_SLEEP_WAITER)
            return result
    except ValueError:
         result = f"Invalid BIN!"
         return result
