# Investment Analysis

This project compares the historical risk and return of US equities,
UK equities, global equities, gold and US investment-grade bonds from
January 2021 to December 2025.

## Main findings

1. Gold generated the highest annualised return during the period.
2. US Equities experienced the greatest annualised volatility.
3. Global Equities had the largest maximum drawdown.
4. The equal-weighted portfolio produced an annualised return of 11.13%
   with annualised volatility of 9.40%.
5. The portfolio achieved a Sharpe ratio of 0.97, approximately equal to Gold and higher than the other 4 assets, suggesting that diversification improved risk-adjusted performance over the historical period.
6. US and Global Equities were highly correlated at 0.98, meaning they provided relatively little diversification from each other. In contrast, Gold and US Bonds had much lower correlations with the equity assets. Combining these assets therefore reduced the extent to which the portfolio moved with any single equity market.

## Diversification

The correlation matrix shows that US Bonds had a relatively low
correlation (-0.02) with UK Equities. This helped diversify the portfolio because
the two assets did not move in exactly the same direction.

## Limitations

- Historical performance does not guarantee future performance.
- The results depend on the selected start and end dates.
- The model assumes equal portfolio weights.
- The portfolio does not account for transaction costs or taxes.
- The assumed risk-free rate is fixed at 2%.
- The ETFs trade in different currencies, so the comparison does not
  fully isolate currency effects.
- The portfolio assumes daily rebalancing back to equal weights, which may not be realistic in practice

## Conclusion

Over the 2021–2025 period, Gold was the strongest-performing individual asset, producing both the highest annualised return and a Sharpe ratio of approximately 0.97. US equities also generated relatively high returns but had the greatest annualised volatility, while global equities experienced the largest maximum drawdown. US bonds had the lowest volatility but produced a negative annualised return over the period. The equal-weighted portfolio did not achieve the highest absolute return, but combining assets with different return patterns reduced annualised volatility to 9.40% while still generating an 11.13% annualised return. Its Sharpe ratio of 0.97 therefore suggests that diversification improved the overall risk-return trade-off compared with most of the individual assets, although the results are specific to this historical period.