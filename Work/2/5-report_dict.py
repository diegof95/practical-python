# Exercise 2.5

from pprint import pprint
from csv import reader

def read_portfolio(file_name:str) -> list:
  """Opens a given portfolio, which is a csv file, and reads it into a list of dictionarys
  Each dictionary has the columns as keys."""

  portfolio = []
  with open(file_name, 'r') as file:
    rows = reader(file)
    headers = next(rows)
    for row in rows:
      dictionary = {
        headers[0]: row[0],
        headers[1]: int(row[1]),
        headers[2]: float(row[2])
      }
      portfolio.append(dictionary)
  return portfolio

print("List of dicts, each dict is a row of the portfolio, with keys indicating column:")
pprint(read_portfolio('../Data/portfolio.csv'))