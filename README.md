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
