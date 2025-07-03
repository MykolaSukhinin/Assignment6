import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd 

Tesla=yf.Ticker("TSLA")
df = Tesla.history(period= '6mo')
df = df[['Close']].copy()

df['sma10'] = df['Close'].rolling(window=10).mean()
df['bma40'] = df['Close'].rolling(window=40).mean()

df['Signal'] = 'hold'
df.loc[(df['sma10'] > df['bma40']) & (df['sma10'].shift(1) <= df['bma40'].shift(1)), 'Signal'] = 'buy'
df.loc[(df['sma10'] < df['bma40']) & (df['sma10'].shift(1) >= df['bma40'].shift(1) ), 'Signal'] = 'sell'
 


print(df.tail(50))
balance = 1000
stocks = 0
bp= None
for i in range(len(df)):
    if df['Signal'].iloc[i] == 'buy':
        stocks = balance / df['Close'].iloc[i]
    elif df['Signal'].iloc[i] == 'sell':
        balance = stocks * df['Close'].iloc[i]
print( 'Прибуток:', balance-1000)


plt.plot(df['Close'])
plt.plot(df['sma10'])
plt.plot(df['bma40'])

plt.xlabel('date')
plt.ylabel('price')
plt.title('TSLA')

plt.show()





