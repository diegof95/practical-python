""" Selecting certain columns from a file to read. List and dict compreh. """

import csv
from pprint import pprint

def read_porfolio(file_name:str) -> tuple:
  """ Read a portfolio from a file, taking Stock name, shares and price, as long as
  the portfolio file has this columns. Uses list and dict compreh."""
  with open(file_name, 'r') as file:
    rows = csv.reader(file)
    
    try:
      headers = next(rows)
      select = ['name', 'shares', 'price']
      columns_indices = [headers.index(column) for column in select]
      portfolio_prices = [
        {
          column: row[index]
          for column, index in zip(select, columns_indices)
        }
        for row in rows
      ]
      return (portfolio_prices, select, columns_indices)

    except Exception as e:
      print(f'Hubo un error leyendo el portafolio: {e}')

if __name__ == '__main__':
  
  portfolio_prices, select, columns_indices = read_porfolio('../Data/portfoliodate.csv')
  print(f'Headers and indices for columns wanted: {select} - {columns_indices}')
  print('Portfolio stocks, shares and prices:')
  pprint(portfolio_prices)