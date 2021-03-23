"""


Create a function that takes a range of numbers and returns the sum of each
digit from `start` to `stop`.

### Examples

    digits_sum(1, 10) ➞ 46
    # total numbers in the range are = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    # sum of each digits is = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 1 + 0 = 46
    
    digits_sum(1, 20) ➞ 102
    
    digits_sum(1, 100) ➞ 901

### Notes

`start` and `stop` are inclusive in the range.

"""

def sumdigits(nbr):
    exp = len(str(nbr))
    if exp == 0:
        return 0
    if exp == 1:
        return sum(range(1, nbr + 1  ) )
    digit = nbr//10**(exp-1)
    allnines = 45 * (exp - 1) * 10**(exp - 2) * digit
    firstdigits = sum(range(1, digit  ) ) * 10**(exp-1)
    results = allnines+firstdigits+ digit
    remaining_nbr = nbr - digit *10**(exp - 1) 
    results = results +   sumdigits(remaining_nbr) + remaining_nbr * digit
    return results
def digits_sum(start, stop):
    return sumdigits(stop) - sumdigits(start - 1)

