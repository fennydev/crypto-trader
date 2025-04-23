
#This file is used to fetch the price of the asset in real time. This is done using the ccxt library.
#ccxt is a library which gives interface to many exchange software such as binance, kraken etc.
import ccxt 
#This line im,port assetpair from config.py file. Asset is in BTC/USDT format.

import time #This is used to make the program sleep for a few seconds before fetching the price again.

from config.settings import BINANCE_API_KEY, BINANCE_SECRET, SYMBOL

#This function fetches the price of the asset in real time. It uses the ccxt library to connect to the binance exchange and fetch the price.

exchange = ccxt.binance({
    'apiKey': BINANCE_API_KEY, 
    'secret': BINANCE_SECRET,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'spot',
    },
})
    
def get_price():
    ticker = exchange.fetch_ticker(SYMBOL)
    return ticker['last']  # current market price