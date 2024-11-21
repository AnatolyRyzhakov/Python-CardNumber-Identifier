from flask import Flask

app: Flask = Flask(__name__)

from routes.routes import *

if __name__ == ("__main__"):
    app.run(debug=True)