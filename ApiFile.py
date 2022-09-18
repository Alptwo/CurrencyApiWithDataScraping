from crypt import methods
import DataScraping
from flask import Flask

app = Flask(__name__)
app.config["DEBUG"]

@app.route("/", methods=["GET"])
def home():
    return '''<h1>Kurların anlık TRY karşılıkları</h1> <p>kullandığınız linkin sonunda "/getLiveExchangeRate" ekleyerek anlık kurlara erişebilirsiniz.</p>'''

@app.route("/getLiveExchangeRate", methods=["GET"])
def getLiveData():
    return DataScraping.getCurrencyRates()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)