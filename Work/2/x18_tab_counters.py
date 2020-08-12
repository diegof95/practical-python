# Exercise 2.18

""" Holdings (total number of shares per stock) on a porfolio,
    combining holdings of various portafolios. Using Counters. """

from collections import Counter
from x4_report import read_portfolio

portfolio1 = read_portfolio('../Data/portfolio.csv')
portfolio2 = read_portfolio('../Data/portfolio2.csv')

holdings1 = Counter()
holdings2 = Counter()

for name, shares, price in portfolio1:
  holdings1[name] += shares

for name, shares, price in portfolio2:
  holdings2[name] += shares

print(f'Holdings on portfolio 1: {holdings1}')
print(f'Holdings on portfolio 2: {holdings2}')

print(f'IBM shares on portfolio 1: {holdings1["IBM"]}')
print(f'AA shares on portfolio 2: {holdings2["AA"]}')

print(f'Holdings on both portfolios (combined): {holdings1 + holdings2}')