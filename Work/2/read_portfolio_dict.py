from csv import reader

def read_portfolio(file_name:str) -> list:
  """Opens a given portfolio, which is a csv file, and reads it into a list of dictionarys
  Each dictionary has the columns as keys. Acepts portfolios with other columns,
  if it contains shares and price columns."""
  
  portfolio = []
  with open(file_name, 'r') as file:
      rows = reader(file)
      headers = next(rows)
      for row in rows:
        data = dict(zip(headers, row))
        portfolio.append(data)
  return portfolio