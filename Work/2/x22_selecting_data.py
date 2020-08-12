""" Extracting / selecting data. """

from read_portfolio_dict import read_portfolio

portfolio = read_portfolio('../Data/porfoliodate.csv')

stocks_shares = [ (stock['name'], stock['shares']) for stock in portfolio ]
stock_names = { stock['name'] for stock in portfolio }
holdings = { name: 0 for name in stock_names }

for stock in portfolio:
  holdings[stock['name']] += int(stock['shares'])

print(f'Stock and shares of portfolio: {stocks_shares}')
print(f'Stock names using set compreh: {stock_names}')
print(f'Stock holdings using set, dict compreh and for loop: {holdings}')