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
    curdigit = 0
    final = ""
    while n > 0:
        curdigit = n % 10
        n = n // 10
        final = str(curdigit ** 2) + final
​
    final = int(final)
    print(final)
    return final

