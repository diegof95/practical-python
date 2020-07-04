# pcost_zip.py
#
# Exercise 1.28

import gzip

with gzip.open('../Data/portfolio.csv.gz', 'r') as file:
    total = 0
    print('portfolio data from gzip, as byte-strings by default:')
    for line in file:
        print(line)

print('-----------')

with gzip.open('../Data/portfolio.csv.gz', 'rt') as file:
    total = 0
    print('portfolio data from gzip as strings:')
    for line in file:
        print(line)