import requests
from datetime import datetime
from flask import Flask
import BackgroundTasks
import threading
import logging


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app = Flask(__name__)

def bgJob():
    thread = threading.Thread(target=BackgroundTasks.StartChecking)
    thread.start()

@app.route('/',methods = ['GET'])
def get_current_data(coin='BTC', tocoin='USD'):
    """
    The function `get_current_data` retrieves the current value of a specified cryptocurrency in a
    specified currency and returns a formatted string with the value and current time.
    
    :param coin: The 'coin' parameter is used to specify the cryptocurrency for which you want to get
    the current value. By default, it is set to 'BTC', which stands for Bitcoin. You can change it to
    any other cryptocurrency symbol like 'ETH' for Ethereum or 'XRP' for Ripple, defaults to BTC
    (optional)
    :param tocoin: The 'tocoin' parameter is the currency in which you want to get the value of the
    cryptocurrency. In the given code, the default value for 'tocoin' is 'USD', which means it will
    return the value of the cryptocurrency in US dollars. However, you can change the value of, defaults
    to USD (optional)
    :return: a string that includes the current value of Bitcoin in USD and the current time in UTC.
    """
    url = 'https://min-api.cryptocompare.com/data/price'    
    parameters = {'fsym': coin,'tsyms': tocoin }
    req = requests.get(url,params=parameters)
    res = req.json()
    currentTime = (datetime.utcnow()).strftime("%d-%m-%Y %H:%MUTC")
    outputline = "ServiceA, Bitcoin value is {value}$ for {currentTime}".format(value=res["USD"],currentTime=currentTime)
    return outputline

with app.app_context():
    bgJob()

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=8080)