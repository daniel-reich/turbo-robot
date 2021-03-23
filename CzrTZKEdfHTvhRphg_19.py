"""


Create a function that takes a string representing a fraction, and return a
string representing that input as a mixed number.

  * Mixed numbers are of the form `1 2/3` — note the space between the whole number portion and the fraction portion.
  * Resulting fractions should be fully reduced (see example #2).
  * If a result is a whole number with no fractional remainder, return only the whole number portion (see example #3).
  * If a result is only fractional with no whole number, return only the fractional portion (see example #4).
  * If a result is negative, the whole number should carry the negative sign. If the result would not have a whole number portion, the numerator of the fractional portion should carry the negative sign (see examples #5 - #7).

### Examples

    mixed_number("5/4") ➞ "1 1/4"
    
    mixed_number("6/4") ➞ "1 1/2"
    
    mixed_number("8/4") ➞ "2"
    
    mixed_number("4/6") ➞ "2/3"
    
    mixed_number("-1/4") ➞ "-1/4"
    
    mixed_number("-5/4") ➞ "-1 1/4"
    
    mixed_number("-8/4") ➞ "-2"

### Notes

All provided inputs will be formatted similarly, negative numbers will be
provided in the numerator portion only, and all inputs will contain no spaces,
invalid characters, or zero denominators.

"""

def mixed_number(frac):
    num = int(frac[:frac.index("/")])
    if num == 0:
        return "0"
    den = int(frac[frac.index("/") + 1:])
    if den != 0:
        integer = abs(num) // den
        new_num = abs(num) % den
        for i in reversed(range(2, new_num + 1)):
            if new_num % i == 0 and den % i == 0:
                new_num //= i
                den //= i
​
    return_str = ""
    if new_num != 0:
        return_str = str(new_num) + "/" + str(den)
    if integer != 0:
        return_str = str(integer) + " " + return_str
        if new_num == 0:
            return_str = return_str[:-1]
    if frac[0] == "-":
        return "-" + return_str
    return return_str

