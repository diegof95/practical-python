""" Inverts a dict representing Stock and Price, switching keys with values.
  Returns Stock with Value of max value stock.
  Warning: If at least two stocks have the same price, they are merged
  and only one stock name its preserved."""

from x17_invert_dict import invert_dict

prices = {
  'GOOG' : 490.1,
  'AA' : 23.45,
  'IBM' : 490.1,
  'MSFT' : 34.23
}

inverted_prices = invert_dict(prices)

max_price, stock = max(inverted_prices.items())

print(f'Stock with max price: {(stock, max_price)}')
print('Warning: If at least two stocks have the same price, they are merged and only one stock name its preserved.')