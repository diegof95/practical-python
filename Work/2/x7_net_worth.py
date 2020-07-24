# Exercise 2.7

""" Calculates total cost and value of the portfolio and its net worth. """

from x5_report_dict import read_portfolio
from x6_prices import read_prices

portfolio = read_portfolio('../Data/portfolio.csv')
prices = read_prices('../Data/portfolio.csv')

portfolio_cost = 0
portfolio_value = 0

for stock in portfolio:
  portfolio_cost += stock['price'] * stock['shares']
  portfolio_value += prices[stock['name']] * stock['shares']

print(f'Total portfolio cost: {portfolio_cost}')
print(f'Total portfolio value: {portfolio_value}')
print(f'Portfolio net-worth : {portfolio_value - portfolio_cost}')