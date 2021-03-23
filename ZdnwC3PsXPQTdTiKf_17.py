"""


Create a function that takes two numbers and a mathematical operator `+ - / *`
and will perform a calculation with the given numbers.

### Examples

    calculator(2, "+", 2) ➞ 4
    
    calculator(2, "*", 2) ➞ 4
    
    calculator(4, "/", 2) ➞ 2

### Notes

If the input tries to divide by 0, return: `"Can't divide by 0!"`

"""

def calculator(num_1: int, operator: str, num_2: int) -> int:
    if num_2 == 0 and operator == "/":
        return"Can't divide by 0!"
    funcs = {
        "+": int.__add__,
        "-": int.__sub__,
        "*": int.__mul__,
        "/": int.__floordiv__
    }
    return funcs[operator](num_1, num_2)

