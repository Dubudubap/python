import time
import pyupbit
import datetime

def get_target_price(ticker):
    df = pyupbit.get_ohlcv(ticker)
    yesterday = df.iloc[-2]

    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.3
    return target

now = datetime.datetime.now()
mid = datetime.datetime(now.year,now.month,now.day) + datetime.timedelta(1)
target_price = get_target_price('KRW-ETH')

while True:
    now = datetime.datetime.now()
    if mid < now < mid + datetime.timedelta(seconds=10):
        target_price = get_target_price('KRW-ETH')
        mid = datetime.datetime(now.year,now.month,now.day) + datetime.timedelta(1)

    current_price = pyupbit.get_current_price('KRW-ETH')
    print(current_price)
    print(target_price)

    time.sleep(1)