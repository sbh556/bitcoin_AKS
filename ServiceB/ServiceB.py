import requests
from datetime import datetime
from flask import Flask
app = Flask(__name__)

@app.route('/',methods = ['GET'])
def get_current_data(coin='BTC', tocoin='USD'):
# This code is making an HTTP GET request to the Cryptocompare API to get the current price of a
# cryptocurrency.
    url = 'https://min-api.cryptocompare.com/data/price'    
    parameters = {'fsym': coin,'tsyms': tocoin }
    req = requests.get(url,params=parameters)
    res = req.json()
    currentTime = (datetime.utcnow()).strftime("%d-%m-%Y %H:%MUTC")
    outputline = "ServiceB, Bitcoin value is {value}$ for {currentTime}".format(value=res["USD"],currentTime=currentTime)
    return outputline

if __name__ == '__main__':
    app.run(debug=True,host = '0.0.0.0',port=8080)