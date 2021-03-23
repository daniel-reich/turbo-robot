"""


Create a function that squares every digit of a number.

### Examples

    square_digits(9119) ➞ 811181
    
    square_digits(2483) ➞ 416649
    
    square_digits(3212) ➞ 9414

### Notes

The function receives an integer and must return an integer.

"""

def square_digits(n):
    lst = [int(d) for d in str(n)]
    return int(''.join(str(i**2) for i in lst))

