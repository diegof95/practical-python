from read_portfolio_dict import read_portfolio

""" Using list comprehension for query purposes. """

portfolio = read_portfolio('../Data/portfoliodate.csv')

more_than_100_sh = [stock for stock in portfolio if int(stock['shares']) > 100]

ibm_msft = [stock for stock in portfolio if stock['name'] in {'IBM', 'MSFT'}]

more_than_10000_total_cost = [stock for stock in portfolio if int(stock['shares']) * float(stock['price']) > 10000]

print(f'Stocks with more than 100 shares: {more_than_100_sh}')
print(f'IBM and MSFT stocks: {ibm_msft}')
print(f'Stocks with more than 1000 in total cost: {more_than_10000_total_cost}')