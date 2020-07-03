# pcost_zip.py
#
# Exercise 1.28
import gzip
with gzip.open('Data/portfolio.csv.gz', 'r') as file:
    total = 0
    next(file)
    for line in file:
        print(line)
print(total)