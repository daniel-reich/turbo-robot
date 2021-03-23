"""


Create a function that takes two integers and returns `true` if a digit
repeats three times in a row at any place in `num1` **AND** that same digit
repeats two times in a row in `num2`.

### Examples

    trouble(451999277, 41177722899) ➞ True
    
    trouble(1222345, 12345) ➞ False
    
    trouble(666789, 12345667) ➞ True
    
    trouble(33789, 12345337) ➞ False

### Notes

You can expect every test case to contain exactly two integers.

"""

def trouble(num1,num2):
    x=['111','222','333','444','555','666','777','888','999','000']
    a=str(num1)
    b=str(num2)
    y=[i for i in x if i in a]
    if y==[]:
        return False
    z=b.count(y[0][:2])
    if z>=1:
        return True
    else:
        return False

