import time
import pyupbit
import datetime

access = "ns9oEj300ASmz7rsWu1bo4sbaWvaqeyQ2RRbCfj2"
secret = "30k0Foj6Y8vpP1xMLEhVyq9j79zaChDxH7ix61dY"

def bull_market(ticker):
    df = pyupbit.get_ohlcv(ticker)
    ma5 = df['close'].rolling(window=7).mean()
    price = pyupbit.get_current_price(ticker)
    last_ma5 = ma5[-2]

    if price > last_ma5:
        return True
    else:
        return False


def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-ETH")
        end_time = start_time + datetime.timedelta(days=1)
        

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            is_bull = bull_market('KRW-ETH')
            target_price = get_target_price("KRW-ETH", 0.0001)
            current_price = get_current_price("KRW-ETH")
            if target_price < current_price and is_bull:
                krw = get_balance("KRW")
                if krw > 0:
                    upbit.buy_market_order("KRW-ETH", krw*0.9995)

        else:
            btc = get_balance("ETH")
            if btc > 0:
                upbit.sell_market_order("KRW-ETH", btc*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)