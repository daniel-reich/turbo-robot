"""


Create a function that takes a mathematical expression as a string, list of
numbers on which the mathematical expression is to be calculated and return
the result as a list of string.

### Examples

    mathematical("f(y)=y+1",[1,2]) ➞ ["f(1)=2","f(2)=3"]
    
    mathematical("f(y)=y^2",[1,2,3]) ➞ ["f(1)=1","f(2)=4","f(3)=9"]
    
    mathematical("f(y)=yx3",[1,2,3]) ➞ ["f(1)=3","f(2)=6","f(3)=9"]

### Notes

  * List of numbers are positive integers.
  * In the algebraic expression x = `*`

"""

def mathematical(exp, numbers):
    final_array = []
    array = []
    array.append(exp[5:6])
    array.append(exp[6:7])
    array.append(exp[7:])
    for number in numbers:
        result = 0
        if array[1] == '+':
            result += number + int(array[2])
        elif array[1] == '-':
            result += number - int(array[2])
        elif array[1] == '^':
            result += number**int(array[2])
        elif array[1] == 'x':
            result += number*int(array[2])
        elif array[1] == '/':
            result += int(number/int(array[2]))
        final_array.append("f({})={}".format(number, result))
    return final_array

