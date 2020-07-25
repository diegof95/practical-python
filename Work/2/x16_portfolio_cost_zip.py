# Exercise 2.16

import csv

def portfolio_cost(filename:str) -> float:
  """ Returns the cost of buying all the shares in a portfolio
  It shows if there is an error on some row with the row number
  Acepts portfolios with other columns, if it contains shares and price columns."""

  with open(filename, 'r') as file:
    rows = csv.reader(file)
    headers = next(rows)
    total = 0
    for r_number, row in enumerate(rows):
      data = dict(zip(headers, row))
      try:
        total += int(data['shares']) * float(data['price'])
      except Exception as e:
        return f'Hubo un error {e} en {r_number}. Error row: {row}'
    return total

if __name__ == '__main__':
  msg = 'Select file to read portfolio:\n\t1(default): portfolio.csv\n\t2:portfoliodate.csv\n\t3:missing.csv\n'
  file_name = input(msg) or '1'

  cost = portfolio_cost('../Data/portfolio.csv')
  if file_name == '2':
    cost = portfolio_cost('../Data/portfoliodate.csv')
  elif file_name == '3':
    cost = portfolio_cost('../Data/missing.csv')

  print(f'Total cost of buying all shares listed in protfolio file:\n {cost}')