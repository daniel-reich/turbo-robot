"""


 **Mubashir** created a function that takes two numbers `a` and `b` and an
operator `o`. His function should return the result of the corresponding
mathematical function on both numbers. If the operator is not one of the
specified characters `+, -, /, *`, or if there is a division by zero, the
function should return `None`. Help him by fixing the code in the code tab to
pass this challenge.

Look at the examples below to get an idea of what the function should do:

### Examples

    basic_calculator(2, '+',  4) ➞ 6
    
    basic_calculator(6, '-', 5) ➞ 1
    
    basic_calculator(12, '/', 3) ➞ 4
    
    basic_calculator(3, '*', 4) ➞ 12
    
    basic_calculator(1, '/', 0) ➞ None
    # Division by zero is not possible
    
    basic_calculator(1, 'x', 0) ➞ None
    # 'x' is not an operator

### Notes

N/A

"""

def basic_calculator(a, o, b):
    result = 0
    if(o == "+"):
        return a + b
    elif(o == "-"):
        return a - b
    elif(o == "/" and b != 0):
        return a / b
    elif(o == "*"):
        return a * b
    return None

