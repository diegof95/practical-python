

from x17_invert_dict import invert_dict

prices = {
  'GOOG' : 490.1,
  'AA' : 23.45,
  'IBM' : 91.1,
  'MSFT' : 34.23
}

inverted_prices = invert_dict(prices)

prices_max = max(inverted_prices.items())

print(prices_max)