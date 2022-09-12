import json
from urllib import response
import bs4
import requests

def  getCurrencyRates():

    bloomberght = "https://www.bloomberght.com/"
    pagedata = requests.get(bloomberght)
    soup = bs4.BeautifulSoup(pagedata.text, "html.parser")
    currentCurrencyRates = soup.findAll("small", class_= "value LastPrice")
    #0 XU100 (BIST100) #1 USDTRY #2 EURTRY #3 EURUSD #4 TAHVIL2Y (2 YILLIK FAİZ) #5 XAU (ALTIN ONS) #6 BRENT PETROL #7 BALTIK KURU YÜK ENDEKSİ
    currentRatesDict = {
        "BIST100": currentCurrencyRates[0].text,
        "USDTRY": currentCurrencyRates[1].text,
        "EURTRY": currentCurrencyRates[2].text,
        "EURUSD": currentCurrencyRates[3].text,
        "XAU": currentCurrencyRates[5].text
    }

    jsonParsedData = json.dumps(currentRatesDict)
    return jsonParsedData