# Exercise 2.15

import csv

def portfolio_cost(filename:str) -> float:
  """ Returns the cost of buying all the shares in a portfolio
  It shows if there is an error on some row with the row number"""

  with open(filename, 'r') as file:
    rows = csv.reader(file)
    next(rows)
    total = 0
    for r_number, row in enumerate(rows):
      try:
        total += int(row[1]) * float(row[2])
      except Exception as e:
        return f'Hubo un error {e} en {r_number}. Error row: {row}'
    return total

if __name__ == '__main__':
  msg = 'Select file to read portfolio:\n\t1(default): portfolio.csv\n\t2:missing.csv\n'
  file_name = input(msg) or '1'

  cost = portfolio_cost('../Data/portfolio.csv')
  if file_name == '2':
    cost = portfolio_cost('../Data/missing.csv')

  print(f'Total cost of buying all shares listed in protfolio file:\n {cost}')