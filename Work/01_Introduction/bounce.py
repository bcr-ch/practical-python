#!/usr/local/bin/python3

height = 100.0
ratio = 3.0 / 5.0
count = 10
bounce = 1

while bounce <= count:
    height = height * ratio
    print(bounce, round(height, 4))
    bounce += 1
