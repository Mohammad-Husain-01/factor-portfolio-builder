import pandas as pd
import numpy as np

def build_portfolio(factor_data, prices_m, top_n=30):
    portfolio_returns = []

    dates = list(factor_data.keys())
    dates.sort()

    prev_weights = None

    for i in range(1, len(dates)):
        date = dates[i]
        prev_date = dates[i-1]

        df = factor_data[prev_date].sort_values("score", ascending=False)
        selected = df.index[:top_n]

        weights = pd.Series(1/len(selected), index=selected)

        # Calculate return for the month
        monthly_returns = prices_m.pct_change().loc[date]
        ret = (weights * monthly_returns.reindex(weights.index).fillna(0)).sum()

        portfolio_returns.append(ret)

    return pd.Series(portfolio_returns, index=dates[1:])
