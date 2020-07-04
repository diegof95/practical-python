

def portfolio_cost(filename:str) -> float:
    """ Returns the cost of buying all the shares in a portfolio """

    with open(filename, 'r') as file:
        total = 0
        next(file)
        for line in file:
            row = line.split(',')
            try:
                total += int(row[1]) * float(row[2])
            except Exception as e:
                return f'Hubo un error: {e}'
        return total

msg = 'Select file to read portfolio:\n\t1(default): portfolio.csv\n\t2:missing.csv\n'
file_name = input(msg) or '1'

cost = portfolio_cost('../Data/portfolio.csv')
if file_name == '2':
    cost = portfolio_cost('../Data/missing.csv')
print(f'Total cost of buying all shares listed in protfolio file: {cost}')