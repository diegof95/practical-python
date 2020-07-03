# mortgage_extra_payment.py
#
# Exercise 1.8

print("""Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage,
Stock Investment, and Bitcoin trading corporation.
The interest rate is 5% and the monthly payment is $2684.11.
Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage.
Get the total amount that Dave will have to pay over the life of the mortgage and number of months to do so.\n
""")

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 1
extra_payment = 1000

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    if months <= 12:
        principal -= extra_payment
        total_paid += extra_payment
    months += 1

print('Total paid:', total_paid, 'Months:', months)