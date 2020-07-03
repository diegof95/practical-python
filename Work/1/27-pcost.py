# pcost.py
#
# Exercise 1.27

with open('Data/portfolio.csv', 'r') as file:
    total = 0
    next(file)
    for line in file:
        row = line.split(',')
        total += int(row[1]) * float(row[2])
print(total)