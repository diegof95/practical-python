from read_portfolio_dict import read_portfolio

def portfolio_cost(filename:str) -> float:
  """ Returns the cost of buying all the shares in a portfolio
  Reads the portfolio file to a list of dict and uses list comprehensions."""
  portfolio = read_portfolio(filename)
  try:
    total_cost = sum([int(stock['shares']) * float(stock['price']) for stock in portfolio])
  except:
    return f'Hubo un error: {e}'
  return total_cost

if __name__ == '__main__':
  total_cost = portfolio_cost('../Data/portfolio.csv')
  print(f'Total cost of buying all shares listed in protfolio :\n {total_cost:0.2f}')