import pyupbit

def bull_market(ticker):
    df = pyupbit.get_ohlcv(ticker)
    ma5 = df['close'].rolling(window=7).mean()
    price = pyupbit.get_current_price(ticker)
    last_ma5 = ma5[-2]

    if price > last_ma5:
        return True
    else:
        return False

is_bull = bull_market('KRW-ETH')
if is_bull : 
    print('상승장')
else:
    print('nope')