# Factor Portfolio Builder  
A quantitative factor-investing model built in Python that ranks stocks on multiple factors, constructs a portfolio, and backtests its performance.

## Overview
This project implements a simple multi-factor investing model using Python.  
It downloads price data, computes factor scores, builds a long-only portfolio, and evaluates performance through a backtesting engine.

The aim of the project is to demonstrate:
- working with financial data in Python  
- building a factor scoring framework  
- constructing portfolios based on quantitative signals  
- running monthly rebalanced backtests  
- generating performance results and charts  

This project was created as part of my learning process in quantitative finance and Python programming.

## Features
- Data download using `yfinance`  
- Factor calculations for:
  - Momentum  
  - Value  
  - Size  
  - Quality  
  - Low Volatility  
- Combined factor score and ranking system  
- Monthly portfolio rebalancing  
- Simple backtesting engine  
- Performance output chart saved in `/results`  

## Project Structure
factor-portfolio-builder/
│── src/
│ ├── data_download.py
│ ├── factor_engine.py
│ ├── portfolio.py
│ └── backtest.py
│── run.py
│── requirements.txt
│── README.md
│── data/ (empty, will store raw data)
│── results/ (stores performance chart)

## How to Run the Project

### 1. Install dependencies
Run the following command:
pip install -r requirements.txt

### 2. Run the backtest
python run.py

The script will:
- download data  
- calculate factor signals  
- build a portfolio  
- run the backtest  
- save a performance chart to `/results/performance.png`  

## Example Output
The backtest will generate a performance chart that illustrates how the factor portfolio would have performed over time.

## Skills Demonstrated
- Python programming  
- Financial data analysis  
- Factor modelling  
- Backtesting frameworks  
- Portfolio construction  
- Use of `pandas`, `numpy`, and `matplotlib`  

## Future Improvements
- Add transaction costs  
- Add long/short portfolios  
- Add more factor definitions  
- Improve weighting methodology  
- Expand visualisation suite  
