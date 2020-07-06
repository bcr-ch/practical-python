#!/usr/local/bin/python3


def portfolio_cost(filename):
    totalcost = 0.0

    with open(filename, 'rt') as f:
        next(f)
        for line in f:
            rows = line.split(',')
            price = float(rows[2])
            try:
                number = float(rows[1])
            except ValueError:
                print("Couldn't parse", line)
            totalcost += price*number
    return totalcost

mytotal = portfolio_cost('../Data/portfolio.csv')
print('Total Cost:', mytotal)
