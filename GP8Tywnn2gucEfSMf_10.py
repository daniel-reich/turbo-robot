"""


Create a function that takes a number as an argument and returns the
appropriate error message. You should do this without using the `switch` or
`if` statements.

The input error will be 1 to 5:

    1 >> "Check the fan"
    2 >> "Emergency stop"
    3 >> "Pump Error"
    4 >> "c"
    5 >> "Temperature Sensor Error"

For any other value, return `101` (you can use an `if` statment here).

### Examples

    error(1) ➞ "Check the fan: e1"
    
    error(2) ➞ "Emergency stop: e2"
    
    error(3) ➞ "Pump Error: e3"

### Notes

Do this **without** using the `switch` or `if` statements.

"""

def error(n):
    d = {1:"Check the fan",2:"Emergency stop", 3:"Pump Error", 4:"c", 5:"Temperature Sensor Error"}
    return d[n] + ": e{}".format(n) if n>=1 and n <= 5  else 101

