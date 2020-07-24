# Exercise 2.12

""" Prints a table with the report of stock price changes """

from x5_report_dict import read_portfolio
from x6_prices import read_prices
from x9_report_price_change import make_report

if __name__ == '__main__':
  portfolio = read_portfolio('../Data/portfolio.csv')
  prices = read_prices('../Data/prices.csv')
  report = make_report(portfolio,prices)
  print('%10s %10s %10s %10s' % report[0])
  separators = ('---------',)*4
  print('%10s %10s %10s %10s' % separators)
  for row in report[1:]:
    print('%10s %10d %10.2f %10.2f' % row)