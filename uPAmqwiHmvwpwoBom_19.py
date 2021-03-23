"""


Create a function that takes an Arabic number and converts it into a Roman
number.

### Examples

    convert_to_roman(2) ➞ "II"
    
    convert_to_roman(12) ➞ "XII"
    
    convert_to_roman(16) ➞ "XVI"

### Notes

  * All roman numerals should be returned as uppercase.
  * The largest number that can be represented in this notation is 3,999.

"""

# Totally not a brute force technique xd
def convert_to_roman(n):
    romans = ''
    if n // 1000:
        m = n // 1000
        romans += 'M' * m
        n -= 1000 * m
    if n >= 900:
        romans += 'CM'
        n -= 900
    if n // 500:
        d = n // 500
        romans += 'D' * d
        n -= 500 * d
    if n >= 400:
        romans += 'CD'
        n -= 400
    if n // 100:
        c = n // 100
        romans += 'C' * c
        n -= 100 * c
    if n >= 90:
        romans += 'XC'
        n -= 90
    if n // 50:
        l = n // 50
        romans += 'L' * l
        n -= 50 * l
    if n >= 40:
        romans += 'XL'
        n -= 40
    if n // 10:
        x = n // 10
        romans += 'X' * x
        n -= 10 * x
    if n == 9:
        romans += 'IX'
        n -= 9
    if n >= 5:
        romans += 'V'
        n -= 5
    if n == 4:
        romans += 'IV'
        n -= 4
    if n:
        romans += 'I' * n
    return romans

