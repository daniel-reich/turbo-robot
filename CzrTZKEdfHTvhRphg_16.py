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

def get_factors(txt):
    return [i for i in range(1, int(txt)+1) if int(txt) % i == 0 and i != 1]
def simplify(txt):
    f1 = get_factors(txt[0])
    f2 = get_factors(txt[1])
    total = 1
    for i in f1:
        if i in f2:
            if i > total:
                total = i
    num1 = int(int(txt[0]) / total)
    num2 = int(int(txt[1]) / total)
    return (num1, num2)
def mixed_number(txt):
    txt = txt.split('/')
    if (int(txt[0]) / int(txt[1])) % 1 == 0:
        return str(int(int(txt[0]) / int(txt[1])))
    else:
        neg = False
        for i in range(len(txt)):
            if '-' in str(txt[i]):
                txt[i] = txt[i][1:]
                neg = True
        nums = simplify(txt)
        num1,num2 = nums[0],nums[1]
        if num1 > num2:
            print('hi')
            whole = int(num1) // int(num2)
            mod = int(num1) % int(num2)
            if neg:
                return '-' + str(whole) + ' ' + str(mod) + '/' + str(num2)
            else:
                return str(whole) + ' ' + str(mod) + '/' + str(num2)
        else:
            if not neg:
                return str(num1) + '/' + str(num2)
            else:
                return '-' + str(num1) + '/' + str(num2)

