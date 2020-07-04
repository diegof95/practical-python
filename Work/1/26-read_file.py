

with open('../Data/portfolio.csv', 'rt') as f:
   data = f.read()

"""
data is a string that contains all the file text:

'name,shares,price\n"AA",100,32.20\n"IBM",50,91.10\n"CAT",150,83.44\n"MSFT",200,51.23\n"GE",95,40.37\n"MSFT",50,65.10\n"IBM",100,70.44\n'

print() outputs it formated
"""

print(f'String with all data from portfolio.csv (formated by print())\n{data}')