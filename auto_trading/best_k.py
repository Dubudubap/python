import pyupbit
import numpy as np


def get_ror(k):
    df = pyupbit.get_ohlcv("KRW-ETH", interval="second1", count = 3600
    )
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'],
                         1)

    ror = df['ror'].cumprod()[-2]
    return ror


def best_k():
    bestK = 0
    bestRor = 0
    ks = []
    for k in range(1,10,1):
        ror = get_ror(k/10)
        ks.append(ror)
        print("%f %f" % (k/10, ror))
        if bestRor < ror :
            bestRor = ror
            bestK = k
    return bestK
df = pyupbit.get_ohlcv('KRW-ETH', interval="second1", count=360)
print(best_k())
print(df)
