from collections import deque

# core/strategy.py

from collections import deque

# Store previous prices for trend detection
price_window = deque(maxlen=3)

def decide_action(current_price: float) -> str:
    """
    Very basic price trend strategy:
    - If price has been rising -> buy
    - If price has been falling -> sell
    - Else -> hold
    """
    price_window.append(current_price)

    if len(price_window) < 3:
        return "hold"

    if price_window[-1] > price_window[-2] > price_window[-3]:
        return "buy"
    elif price_window[-1] < price_window[-2] < price_window[-3]:
        return "sell"
    else:
        return "hold"
