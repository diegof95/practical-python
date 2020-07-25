# Exercise 2.17

import pprint

def invert_dict(dictionary:dict) -> dict:
  """ Takes a dictionary and returns a dict, inverted respect to key, values."""

  keys = dictionary.keys()
  values = dictionary.values()
  inverted_dict = dict(zip(values, keys))

  return inverted_dict

if __name__ == '__main__':
  
  prices = {
    'GOOG' : 490.1,
    'AA' : 23.45,
    'IBM' : 91.1,
    'MSFT' : 34.23
  }

  pprint(f'Prices dict: {prices}')
  inverted_prices = invert_dict(prices)
  pprint(f'Prices inverted dict: {inverted_prices}')