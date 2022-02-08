import pyupbit
import numpy as np


def get_ror(k=0.5):
    df = pyupbit.get_ohlcv("KRW-ETH", count = 7
    )
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'],
                         1)

    ror = df['ror'].cumprod()[-2]
    return ror


def best_k(ror):
    ks = []
    for k in np.arange(0.1, 1.0, 0.1):
        ror = get_ror(k)
        ks.append(ror)
        print("%f %f" % (k, ror))
        bestK = ks.index(max(ks))
        ks.clear()
    return bestK

print(best_k(get_ror()))