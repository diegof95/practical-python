# Exercise 2.4

from csv import reader

def read_portfolio(file_name:str) -> list:
  """Opens a given portfolio, which is a csv file, and reads it into a list of tuples"""

  portfolio = []
  with open(file_name, 'r') as file:
    rows = reader(file)
    next(rows)
    for row in rows:
      portfolio.append((row[0], int(row[1]), float(row[2])))
  return portfolio

print("List of tuples, each tuple is a row of the portfolio:")
print(read_portfolio('../Data/portfolio.csv'))