import os
from dotenv import load_dotenv

load_dotenv()

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")

SYMBOL ='BTCUSDT'

INTERVAL_MINUTES = 1
INTERVAL_MINUTES = 5
TRADE_AMOUNT_USD = 20

# RSI strategy config (if you’ll use RSI)
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30

# Enable real trades
REAL_MODE = False  # Set True to go live!

# Telegram alert config
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Logging / State tracking
STATE_FILE = "logs/state.json"