#!/usr/bin/env python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    if len(sys.argv) < 2:
        print("Usage: ./factorial.py <non-negative integer>")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        print(factorial(n))
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
