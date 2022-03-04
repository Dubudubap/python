from itertools import count
import pyupbit

def bull_market(ticker):
    df = pyupbit.get_ohlcv(ticker,interval="minute5",count=288)
    print(df)
    ma5 = df['close'].rolling(window=12).mean()
    print(ma5)
    price = pyupbit.get_current_price(ticker)
    last_ma5 = ma5[-1]
    print(last_ma5)
    print(price)
    if price > last_ma5:
        return True
    else:
        return False

is_bull = bull_market('KRW-ETH')
if is_bull : 
    print('상승장')
else:
    print('nope')