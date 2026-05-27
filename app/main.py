import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

ticker = "AAPL"

data = yf.download(ticker, start="2023-01-01", end="2024-01-01")

print(data.head())

plt.figure(figsize=(12, 6))
plt.plot(data['Close'])

plt.title(f"{ticker} Closing Prices")
plt.xlabel("Date")
plt.ylabel("Price")

plt.show()