"""
Calculator library containing basic math operations.
"""


def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def multiply(first_term, second_term):
    return first_term * second_term


def divide(dividend, divisor):
    if divisor == 0:
        raise ValueError("Division by zero is not allowed")
    return dividend / divisor

