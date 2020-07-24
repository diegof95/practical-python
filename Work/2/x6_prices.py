# Exercise 2.6

from pprint import pprint
from csv import reader

def read_prices(file_name:str) -> dict:
  """Opens a given set of stocks and corresponding prices, which is a csv file,
  and reads it into a dictionary, with stock name as key and its price as value."""

  prices = {}
  with open(file_name, 'r') as file:
    rows = reader(file)
    for row in rows:
      # Catching the empty list representing the empty row
      try:
        prices[row[0]] = float(row[1])
      except Exception as e:
        pass
  return prices

if __name__ == '__main__':
  print("A dictionary representing stocks and its prices, with stock name as key and its price as value:")
  pprint(read_prices('../Data/prices.csv'))