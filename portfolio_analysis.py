import os

import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

TICKERS = {
    "US Equities": "SPY",
    "UK Equities": "ISF.L",
    "Global Equities": "URTH",
    "Gold": "GLD",
    "US Bonds": "AGG",
}

START_DATE = "2021-01-01"
END_DATE = "2026-01-01"

os.makedirs("data", exist_ok=True)
os.makedirs("charts", exist_ok=True)

# downloading data from Yahoo Finance

raw_data = yf.download(
    list(TICKERS.values()),
    start=START_DATE,
    end=END_DATE,
    auto_adjust=True,
    progress=False,
)

prices = raw_data["Close"].copy()

ticker_to_name = {}

for name, ticker in TICKERS.items():
    ticker_to_name[ticker] = name

prices = prices.rename(columns=ticker_to_name)

prices = prices.dropna()

prices.to_csv("data/asset_prices.csv")
print("Downloaded prices:")
print(prices.head())

# plotting raw prices

plt.figure(figsize=(12, 6))

for asset in prices.columns:
    plt.plot(prices.index, prices[asset], label=asset)

plt.title("Historical Asset Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.tight_layout()
plt.savefig("charts/historical_prices.png")
plt.close()

normalised_prices = prices / prices.iloc[0] * 100

# plotting normalised prices

plt.figure(figsize=(12, 6))

for asset in normalised_prices.columns:
    plt.plot(
        normalised_prices.index,
        normalised_prices[asset],
        label=asset,
    )

plt.axhline(100, linestyle="--", linewidth=1)
plt.title("Growth of an Initial £100 Investment")
plt.xlabel("Date")
plt.ylabel("Investment Value")
plt.legend()
plt.tight_layout()
plt.savefig("charts/normalised_performance.png")
plt.close()

normalised_prices.to_csv("data/normalised_prices.csv")

# calculating daily returns

daily_returns = prices.pct_change().dropna()

daily_returns.to_csv("data/daily_returns.csv")

print("\nDaily returns:")
print(daily_returns.head())

# calculating performance stats

TRADING_DAYS = 252

total_returns = prices.iloc[-1] / prices.iloc[0] - 1

number_of_years = len(prices) / TRADING_DAYS

annualised_returns = (
    prices.iloc[-1] / prices.iloc[0]
) ** (1 / number_of_years) - 1

annualised_volatility = (
    daily_returns.std() * (TRADING_DAYS ** 0.5)
)

RISK_FREE_RATE = 0.02

sharpe_ratios = (
    annualised_returns - RISK_FREE_RATE
) / annualised_volatility

running_maximum = normalised_prices.cummax()
drawdowns = normalised_prices / running_maximum - 1
maximum_drawdowns = drawdowns.min()

summary = pd.DataFrame({
    "Total Return": total_returns,
    "Annualised Return": annualised_returns,
    "Annualised Volatility": annualised_volatility,
    "Sharpe Ratio": sharpe_ratios,
    "Maximum Drawdown": maximum_drawdowns,
})

summary = summary.sort_values(
    by="Sharpe Ratio",
    ascending=False,
)

summary.to_csv("data/performance_summary.csv")

display_summary = summary.copy()

percentage_columns = [
    "Total Return",
    "Annualised Return",
    "Annualised Volatility",
    "Maximum Drawdown",
]

for column in percentage_columns:
    display_summary[column] = (
        display_summary[column] * 100
    ).round(2)

display_summary["Sharpe Ratio"] = (
    display_summary["Sharpe Ratio"].round(2)
)

print("\nPerformance summary:")
print(display_summary)

# plotting maximum drawdowns

plt.figure(figsize=(12, 6))

for asset in drawdowns.columns:
    plt.plot(
        drawdowns.index,
        drawdowns[asset] * 100,
        label=asset,
    )

plt.title("Asset Drawdowns")
plt.xlabel("Date")
plt.ylabel("Drawdown (%)")
plt.legend()
plt.tight_layout()
plt.savefig("charts/drawdowns.png")
plt.close()

# equally weighted portfolio

number_of_assets = len(daily_returns.columns)
equal_weight = 1 / number_of_assets

portfolio_daily_returns = (
    daily_returns * equal_weight
).sum(axis=1)

portfolio_growth = (
    1 + portfolio_daily_returns
).cumprod() * 100

# plotting portfolio performance graph

plt.figure(figsize=(12, 6))

for asset in normalised_prices.columns:
    plt.plot(
        normalised_prices.index,
        normalised_prices[asset],
        label=asset,
    )

plt.plot(
    portfolio_growth.index,
    portfolio_growth,
    label="Equal-Weighted Portfolio",
    linewidth=3,
)

plt.axhline(100, linestyle="--", linewidth=1)
plt.title("Asset and Portfolio Performance")
plt.xlabel("Date")
plt.ylabel("Growth of Initial £100")
plt.legend()
plt.tight_layout()
plt.savefig("charts/portfolio_comparison.png")
plt.close()

# calculating portfolio statistics

portfolio_total_return = portfolio_growth.iloc[-1] / 100 - 1

portfolio_annualised_return = (
    portfolio_growth.iloc[-1] / 100
) ** (1 / number_of_years) - 1

portfolio_volatility = (
    portfolio_daily_returns.std() * (TRADING_DAYS ** 0.5)
)

portfolio_sharpe_ratio = (
    portfolio_annualised_return - RISK_FREE_RATE
) / portfolio_volatility

portfolio_running_maximum = portfolio_growth.cummax()

portfolio_drawdown = (
    portfolio_growth / portfolio_running_maximum - 1
)

portfolio_maximum_drawdown = portfolio_drawdown.min()

portfolio_summary = pd.Series({
    "Total Return": portfolio_total_return,
    "Annualised Return": portfolio_annualised_return,
    "Annualised Volatility": portfolio_volatility,
    "Sharpe Ratio": portfolio_sharpe_ratio,
    "Maximum Drawdown": portfolio_maximum_drawdown,
})

print("\nEqual-weighted portfolio summary:")

for statistic, value in portfolio_summary.items():
    if statistic == "Sharpe Ratio":
        print(f"{statistic}: {value:.2f}")
    else:
        print(f"{statistic}: {value:.2%}")

correlation_matrix = daily_returns.corr()
correlation_matrix.to_csv("data/correlation_matrix.csv")

print("\nCorrelation matrix:")
print(correlation_matrix.round(2))

print("\nAnalysis completed successfully.")
print("Tables were saved in the data folder.")
print("Graphs were saved in the charts folder.")