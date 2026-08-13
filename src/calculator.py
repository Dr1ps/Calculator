import math
from enum import Enum
from typing import Literal

PI = math.pi
E = math.e

type number = int | float
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
operators = ["+", "-", "x", "÷"]


class ShiftDirection(Enum):
    LEFT = 0
    RIGHT = 1


def calculate(expression: str) -> number | None:
    global PI
    if (not expression or expression == ""):
        return None
    expression = buildExpression(expression)
    try:
        result = eval(expression)
    except ZeroDivisionError as e:
        return "Math Error"
    except (NameError, SyntaxError) as e:
        return "Syntax Error"
    else:
        if isinstance(result, (int, float)):
            return result
        return None


def buildExpression(expression: str) -> str:
    global PI
    global E
    expression = expression.replace("EXP", "*10^")
    expression = expression.replace("x", "*")
    expression = expression.replace("×", "*")
    expression = expression.replace("÷", "/")
    expression = expression.replace("^", "**")
    expression = expression.replace("π", "PI")
    expression = expression.replace("e", "E")
    return expression


def add(a: number, b: number) -> number:
    return a + b


def subtract(a: number, b: number) -> number:
    return a - b


def multiply(a: number, b: number) -> number:
    return a * b


def divide(a: number, b: number) -> number:
    return a / b


def module(a: number, b: number) -> number:
    return a % b


def sqrt(a: number) -> number:
    return math.sqrt(a)


def xRoot(a: number, b: number) -> number:
    return a ** (1/b)


def square(a: number) -> number:
    return a ** 2


def power(a: number, b: number) -> number:
    return a ** b


def shiftDecimal(a: number, b: ShiftDirection) -> number:
    if (b.value == 0):
        return a / 10
    if (b.value == 1):
        return a * 10


def exp(a: number, b: number) -> number:
    return a * math.pow(10, b)


def absoluteValue(a: number) -> number:
    if (a < 0):
        return -a
    else:
        return a
