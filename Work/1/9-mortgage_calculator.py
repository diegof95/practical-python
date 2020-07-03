# mortgage_calculator.py
#
# Exercise 1.9

print("""Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage,
Stock Investment, and Bitcoin trading corporation.
The interest rate is 5% and the monthly payment is $2684.11.
Let Dave enter extra payment amount, month where extra payments begins and month when ends.
Get the total amount that Dave will have to pay over the life of the mortgage and number of months to do so.\n
""")


principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 1
extra_payment = float(input('Enter extra_payment value: (1000) ') or '1000')
extra_payment_start_month = int(input('Enter extra_payment start month: (60) ') or '60')
extra_payment_end_month = int(input('Enter extra_payment end month: (108) ') or '48')

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment
    months += 1

print('Total paid:', total_paid, 'Months:', months)