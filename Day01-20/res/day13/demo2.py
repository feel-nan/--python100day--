stocks = {
  'BHP': 56.75,
  'AAPL': 166.35,
  'MSFT': 85.25,
  'GOOG': 210.45,
  'FB': 132.55,
  'AMZN': 338.45,
  'NFLX': 543.25,
  'TSLA': 284.55,
  'NVDA': 235.75,
  'JPM': 156.25,
}
stocks2 = {key: value for key, value in stocks.items() if value > 100}
print(stocks2)  