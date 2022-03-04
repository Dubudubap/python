import pyupbit
import numpy as np

access = "2hun7PER4v7BFbdOwmxmFjAerRXxdylgx2hUq3x9"
secret = "k36NQHbxj3CuVXEHln7beatVNFFA3BFZyIPbqLNC"
upbit = pyupbit.Upbit(access, secret)

df = pyupbit.get_ohlcv("KRW-ETH",interval="minute60",count=24)
 
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

fee = 0

df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print(df)
print('MDD(%): ',df['dd'].max())
