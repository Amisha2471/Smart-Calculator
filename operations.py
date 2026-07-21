#CALCULATOR

import math


def add (a , b):
    """Add two numbers"""
    return a + b


def subtract (a , b):
    """Subtract b from a """
    return a - b



def multiply (a , b):
    """Multiply two numbers"""
    return a * b


def divide (a , b):
    """Divide a by b. Return error message if b is zero."""
    if b == 0:
        return "Error: Cannot be divided by zero!"
    return a / b

def calculator (a , b, operator):
    """
    Dictionart = Key value pair.
    """
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    func = operations.get(operator)
    if func:
        return func(a , b)
    return "Error message : invalid operator!"


# power and root

def power (base ,  exponent):
    "power of numbers"
    return base ** exponent

def square_root(number):
    "square root of number"
    if number < 0:
        return "Error: Cannot find square rootn of negative number!"
    return math.sqrt (number)


#percentage

def percentage (value , total):
    "value = 85 , total = 100 so 85%"
    if total==0:
        return "Error : Total cannot be zero!"
    return (value / total) * 100


def percentage_of (percent , total):
     return (percent / total) * 100


def percentage_change(old_value , new_value):
    if old_value ==0:
        return "Error: old value cannot be zero!"
    change = ((new_value-old_value)/abs(old_value))*100
    return change


#Average

def average(numbers):
    if len(numbers)==0:
        return "Error: No numbers provided!"
    return sum(numbers) / len(numbers)