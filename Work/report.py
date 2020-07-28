#!/usr/local/bin/python3
# report.py
#
# Exercise 2.4
import csv
import sys

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
           d = {
               'name': row[0],
               'price': int(row[1]),
               'cost': float(row[2])
           }
           portfolio.append(d)
    return portfolio

def read_prices(filename)
    prices = []

    with open(pricefile, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            holdings = (row[0], float(row[1]))
            prices.append(holdings)
        return prices

if len(sys.argv) == 3:
    filename = sys.argv[1]
    pricefile = sys.argv[2]
else:
    filename = 'Data/portfolio.csv'
    pricefile = 'Data/prices.csv'
