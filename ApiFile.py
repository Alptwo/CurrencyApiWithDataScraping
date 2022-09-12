from crypt import methods
import DataScraping
from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/getLiveCurrencyData", methods=["GET"])
def getLiveData():
    return DataScraping.getCurrencyRates()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)