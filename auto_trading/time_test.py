import numpy as np
import pyupbit


df = pyupbit.get_ohlcv("KRW_ETH",interval="day",count=10)

print(df)