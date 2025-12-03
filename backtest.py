import pandas as pd
import matplotlib.pyplot as plt
from src.data_download import get_sp500_tickers, download_price_data
from src.factor_engine import monthly_prices, download_fundamentals, compute_factors
from src.portfolio import build_portfolio
import os

def run_backtest():
    # 1) Download
    tickers = get_sp500_tickers()
    prices = download_price_data(tickers)
    prices_m = monthly_prices(prices)

    # 2) Fundamentals
    fundamentals = download_fundamentals(tickers)

    # 3) Factors
    factor_data = compute_factors(prices_m, fundamentals)

    # 4) Portfolio returns
    rets = build_portfolio(factor_data, prices_m)

    # 5) Plot cumulative performance
    cum = (1 + rets).cumprod()

    os.makedirs("results", exist_ok=True)
    cum.plot(figsize=(10,5), title="Factor Portfolio Cumulative Returns")
    plt.savefig("results/performance.png")
    plt.show()

    print(rets.describe())

if __name__ == "__main__":
    run_backtest()
