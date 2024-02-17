import yfinance
import requests
import warnings

warnings.filterwarnings('ignore')
data = yfinance.Ticker('TSLA')
dat = data.history('max')
print(dat.head())

