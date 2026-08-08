import math
from enum import Enum

type number = int | float


class ShiftDirection(Enum):
    LEFT = 0
    RIGHT = 1


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


def power(a: number, b: number) -> number:
    return a ** b


def shiftDecimal(a: number, b: ShiftDirection):
    if (b.value == 0):
        return a / 10
    if (b.value == 1):
        return a * 10
