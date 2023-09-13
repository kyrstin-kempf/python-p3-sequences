#!/usr/bin/env python3

def print_fibonacci(length):

    fib_range = []
    if length > 0:
        fib_range.append(0)
    if length >=2:
        fib_range.append(1)
        for i in range(2, length):
            fib_range.append(fib_range[-1] + fib_range[-2])

    print(fib_range)