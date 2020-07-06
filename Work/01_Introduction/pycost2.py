#!/usr/local/bin/python3

import csv
import sys

def portfolio_cost(filename):
    totalcost = 0.0

    with open(filename, 'rt') as f:
        csv_rows = csv.reader(f)
        next(csv_rows)
        for line in csv_rows:
            price = float(line[2])
            number = float(line[1])
            totalcost += price*number
    return totalcost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = '../Data/portfolio.csv'
mytotal = portfolio_cost(filename)
print('Total Cost:', mytotal)
