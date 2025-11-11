#app/calculator.py 
import math
from typing import Union

Number = Union[int, float]

def sqrt(x: Number) -> float:
    if x < 0:
        raise ValueError("sqrt: negative input")
    return math.sqrt(x)

def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("factorial: input must be integer")
    if n < 0:
        raise ValueError("factorial: negative input")
    # use iterative for large n safety
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def ln(x: Number) -> float:
    if x <= 0:
        raise ValueError("ln: input must be positive")
    return math.log(x)

def power(x: Number, b: Number) -> float:
    # allow non-integer exponent
    return math.pow(x, b)

#change
