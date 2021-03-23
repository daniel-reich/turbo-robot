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

def trouble(num1, num2):
    trips = []
    doubs = []
    for i in range(len(str(num1))-2):
        if str(num1)[i] == str(num1)[i+1] and str(num1)[i] == str(num1)[i+2]:
            trips += [str(num1)[i]]
    for j in range(len(str(num2))-1):
        if str(num2)[j] == str(num2)[j + 1]:
            doubs += [str(num2)[j]]
    out = False
    for each in trips:
        if each in doubs:
            out = True
    return out

