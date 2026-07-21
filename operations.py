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
        return "Error: Cannot divide by zero!"
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
        return "Error: Cannot find square root of negative number!"
    return math.sqrt (number)


#percentage

def percentage (value , total):
    "value = 85 , total = 100 so 85%"
    if total==0:
        return "Error : Total cannot be zero!"
    return round((value/total)*100,2)


def percentage_of (percent , total):
     return (percent * total) / 100


def percentage_change(old_value , new_value):
    if old_value ==0:
        return "Error: old value cannot be zero!"
    change = ((new_value-old_value)/abs(old_value))*100
    return round(change,2)


#Average

def average(numbers):
    if len(numbers)==0:
        return "Error: No numbers provided!"
    return sum(numbers) / len(numbers)


# ==========================
# SCIENTIFIC CALCULATOR
# ==========================
def sine(angle):
    """Returns sine of angle in degrees"""

    result = math.sin(math.radians(angle))

    if abs(result) < 1e-10:
        result = 0

    return round(result, 6)

def cosine(angle):
    """Returns cosine of angle in degrees"""

    result = math.cos(math.radians(angle))

    if abs(result) < 1e-10:
        result = 0

    return round(result, 6)


def tangent(angle):
    """Returns tangent of angle in degrees"""

    # tan(90°), tan(270°), tan(450°)... undefined hote hain
    if angle % 180 == 90:
        return "Error: tan() is undefined for this angle!"

    return round(math.tan(math.radians(angle)), 6)

def logarithm(number):
    """Returns base-10 logarithm"""
    if number <= 0:
        return "Error: Logarithm only defined for positive numbers!"
    return round(math.log10(number), 6)


def natural_log(number):
    """Returns natural logarithm (ln)"""
    if number <= 0:
        return "Error: Natural log only defined for positive numbers!"
    return round(math.log(number), 6)


def factorial(number):
    """Returns factorial"""
    if number < 0:
        return "Error: Factorial of negative number is not possible!"
    if int(number) != number:
        return "Error: Factorial only works for whole numbers!"
    return math.factorial(int(number))

# ==========================
# EXTRA SCIENTIFIC FUNCTIONS
# ==========================

def inverse(number):
    """Returns reciprocal (1/x)"""
    if number == 0:
        return "Error: Cannot divide by zero!"
    return round(1 / number, 6)


def cube(number):
    """Returns cube of a number"""
    return number ** 3


def cube_root(number):
    """Returns cube root of a number"""

    if number >= 0:
        return round(number ** (1/3), 6)
    else:
        return round(-((-number) ** (1/3)), 6)


def modulus(a, b):
    """Returns remainder"""

    if b == 0:
        return "Error: Cannot divide by zero!"

    return a % b


def absolute(number):
    """Returns absolute value"""
    return abs(number)
