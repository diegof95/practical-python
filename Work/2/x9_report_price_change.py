# Exercise 2.12

def make_report(portfolio:list, prices:dict) -> list:
  """ In this report, “Price” is the current share price of the stock
  and “Change” is the change in the share price from the initial purchase price.
  Prices are float numbers without formatting."""
  report = []
  report.append(('Name', 'Shares', 'Price', 'Change'))
  for stock in portfolio:
    row = (
      stock['name'],
      stock['shares'],
      # Use different quotes for dict keys inside or f-string will end
      prices[stock["name"]],
      prices[stock["name"]] - stock["price"],
    )
    report.append(row)
  return report

def make_report_formated(portfolio:list, prices:dict) -> list:
  """ In this report, “Price” is the current share price of the stock
  and “Change” is the change in the share price from the initial purchase price.
  Prices are formatted as floats with 2 decimals."""
  report = []
  report.append(('Name', 'Shares', 'Price', 'Change'))
  for stock in portfolio:
    row = (
      stock['name'],
      stock['shares'],
      # Use different quotes for dict keys inside or f-string will end
      f'{prices[stock["name"]]:0.2f}',
      f'{prices[stock["name"]] - stock["price"]:0.2f}',
    )
    report.append(row)
  return report