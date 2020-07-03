

symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
print('Symbols string:', symbols)

print('1st symbols declaration Id:', id(symbols))

symbols = symbols + 'GOOG'
print('Symbols + "GOOG":', symbols)

print('symbols declaration after concat Id:', id(symbols))
print('Difference in Ids shows inmutability holds on strings')

symbols = symbols[:-4]+ ',' +symbols[-4:]
print('Using string slicing to fix missing ",":', symbols)

symbols = symbols + ',HPQ'
print('Symbols + "HPQ":', symbols)

