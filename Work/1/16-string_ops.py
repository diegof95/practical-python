
symbols = 'AAPL,IBM,MSFT,YHOO,SCO,GOOG,HPQ'

print('Find "MSFT":', symbols.find('MSFT'))

print('symbols[13:17]:', symbols[13:17])

print('Replace "SCO" with "DOA":',symbols.replace('SCO','DOA'))


name = '   IBM   \n'
print('Name:', name)
name = name.strip()   # Remove surrounding whitespace
print('name stripped surrounding spaces:', name)

