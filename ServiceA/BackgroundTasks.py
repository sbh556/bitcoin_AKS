# -*- coding: ascii-*-
import time
import requests
from datetime import datetime

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
    if(not req.ok):
        print("unable to retrive bitcoin value")
        return 0
    res = req.json()
    return res["USD"]

def getBitcoinAvg(bitcoinList):
    """
    The function calculates the average value of a list of bitcoin prices.
    
    :param bitcoinList: A list of bitcoin prices
    :return: The average value of the bitcoinList.
    """
    return sum(bitcoinList)/len(bitcoinList)

def main():
    """
    The main function continuously retrieves the current bitcoin value every minute, stores it in a list
    for the last ten minutes, and calculates and prints the average value if ten minutes have passed.
    """
    lastTenMinutes = []
    while(True):
        bitcoin = get_current_data()
        lastTenMinutes.append(bitcoin)
        currentTime = (datetime.utcnow()).strftime("%d-%m-%Y %H:%MUTC")
        outputline = "current bitcoin value: {value}$ for {currentTime}".format(value=bitcoin,currentTime=currentTime)
        print(outputline)
        if(len(lastTenMinutes) == 10):
            avg = getBitcoinAvg(lastTenMinutes)
            outputline = "The avg of the last 10 minutes: {value}$".format(value=avg)
            print(outputline)
            lastTenMinutes = []
        time.sleep(60)

if __name__ == '__main__':
    main()