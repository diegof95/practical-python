# Exercise 2.18

""" Total number of shares per stock of the porfolio """

from collections import Counter
from x4_report import read_portfolio

portfolio = read_portfolio('../Data/portfolio.csv')

holdings = Counter()

for name, shares, price in portfolio:
  holdings[name] += shares