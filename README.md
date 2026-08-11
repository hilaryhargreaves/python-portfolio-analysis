

# Multi-Asset Portfolio Analysis in Python

## Overview

This project analyses the historical performance of five asset classes:

- US equities
- UK equities
- Global equities
- Gold
- US investment-grade bonds

It compares their returns, volatility, Sharpe ratios, drawdowns and
correlations between January 2021 and December 2025. It also constructs
an equally weighted multi-asset portfolio and evaluates its historical
risk-return performance.

## Project objectives

The project was created to explore:

- How different asset classes performed over the selected period
- The relationship between investment return and volatility
- How maximum drawdown captures downside risk
- Whether combining asset classes improved diversification
- How an equally weighted portfolio compared with individual assets

## Technologies

- Python
- pandas
- matplotlib
- yfinance

## How to run

Install the required packages:

```bash
pip install -r requirements.txt

## Metrics calculated

- Total return
- Annualised return
- Annualised volatility
- Sharpe ratio
- Maximum drawdown
- Return correlations

## Project structure

```text
python-portfolio-analysis/
│
├── portfolio_analysis.py
├── analysis.md
├── README.md
├── requirements.txt
├── data/
└── charts/