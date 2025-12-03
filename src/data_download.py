mport yfinance as yf
import pandas as pd
from tqdm import tqdm
import os

def get_sp500_tickers():
    """Scrape S&P 500 tickers from Wikipedia."""
    table = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
    tickers = table["Symbol"].str.replace(".", "-", regex=False).tolist()
    return tickers

def download_price_data(tickers, start="2015-01-01"):
    """Download daily adjusted close prices for all tickers."""
    data = yf.download(tickers, start=start, progress=False)["Adj Close"]
    return data

def save_data(prices, outpath="data/prices.csv"):
    os.makedirs("data", exist_ok=True)
    prices.to_csv(outpath)
    print(f"Saved price data to {outpath}")

if __name__ == "__main__":
    tickers = get_sp500_tickers()
    prices = download_price_data(tickers)
    save_data(prices)
