#!/usr/local/bin/python3

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = int(input('Starting Month '))
extra_payment_end_month = int(input('Ending Month '))
extra_payment = float(input('Extra Payment '))
month = 0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    if principal < 0:
        payment = payment + principal
        principal = 0
    total_paid = total_paid + payment
    month += 1
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    output = f'{month} {total_paid} {principal}'
    #print(month, total_paid, prinicipal)
    print(output)
    

print('Total paid', round(total_paid, 2), 'in', month, 'months')