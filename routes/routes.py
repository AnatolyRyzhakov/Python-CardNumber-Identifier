from app import app, bin_data
from flask import render_template, request
from core.db_manager import search_bin_in_data_source

@app.route("/", methods=["GET"])
def index():
        return render_template("index.html")

@app.route("/identify", methods=["GET"])
def return_bank_brand_via_bin():
    bin_number = request.args.get("BIN")
    if int(bin_number) > 0:
        bank_brand_name = search_bin_in_data_source(int(bin_number), bin_data)
        result = f"For BIN {bin_number} bank brand name is: {bank_brand_name}"
        return result
    else:
        result = f"Invalid BIN!"
        return result
