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

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
