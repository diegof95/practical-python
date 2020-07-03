# mortgage.py
#
# Exercise 1.7

print("""Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage,
Stock Investment, and Bitcoin trading corporation.
The interest rate is 5% and the monthly payment is $2684.11.
Get the total amount that Dave will have to pay over the life of the mortgage\n""")

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid is', total_paid)