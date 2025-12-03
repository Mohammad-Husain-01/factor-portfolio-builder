mport pandas as pd
import yfinance as yf
import numpy as np
from tqdm import tqdm
import os

def monthly_prices(prices):
    return prices.resample("M").last()

def compute_momentum(prices_m):
    """12-month momentum (return from t-12 to t-1)."""
    return (prices_m / prices_m.shift(12) - 1).shift(1)

def compute_volatility(prices_m):
    returns = prices_m.pct_change()
    return returns.rolling(3).std()   # 3-month volatility

def download_fundamentals(tickers):
    fundamentals = {}

    for t in tqdm(tickers):
        try:
            info = yf.Ticker(t).info
            fundamentals[t] = {
                "marketCap": info.get("marketCap"),
                "priceToBook": info.get("priceToBook"),
                "beta": info.get("beta"),
            }
        except:
            fundamentals[t] = {"marketCap": None, "priceToBook": None, "beta": None}

    return pd.DataFrame(fundamentals).T

def compute_factors(prices_m, fundamentals):
    momentum = compute_momentum(prices_m)
    volatility = compute_volatility(prices_m)

    # Merge static fundamentals into monthly timelines
    combined = pd.DataFrame(index=prices_m.index, columns=prices_m.columns)

    factor_data = {}

    for date in prices_m.index:
        df = pd.DataFrame({
            "momentum": momentum.loc[date],
            "volatility": volatility.loc[date],
            "value": fundamentals["priceToBook"],
            "size": fundamentals["marketCap"],
            "quality": fundamentals["beta"]
        })

        # Normalise (z-score) → makes factors comparable
        df = df.apply(lambda x: (x - x.mean()) / (x.std() + 1e-9))

        # Lower volatility & size are good → multiply by -1
        df["volatility"] *= -1
        df["size"] *= -1

        # Composite factor score
        df["score"] = df.mean(axis=1)

        factor_data[date] = df

    return factor_data

def save_factor_data(factor_data, outpath="data/factors.pkl"):
    os.makedirs("data", exist_ok=True)
    pd.to_pickle(factor_data, outpath)
    print(f"Saved factor data to {outpath}")
