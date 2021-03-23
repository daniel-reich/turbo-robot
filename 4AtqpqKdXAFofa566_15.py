"""


Create a function that takes in a _number as a string_ `n` and returns the
number **without trailing and leading zeros**.

  *  **Trailing Zeros** are the zeros _after_ a decimal point which _don't affect the value_ (e.g. the _last three_ zeros in `3.4000` and `3.04000`).
  *  **Leading Zeros** are the zeros _before_ a whole number which _don't affect the value_ (e.g. the _first three_ zeros in `000234` and `000230`).

### Examples

    remove_leading_trailing("230.000") ➞ "230"
    
    remove_leading_trailing("00402") ➞ "402"
    
    remove_leading_trailing("03.1400") ➞ "3.14"
    
    remove_leading_trailing("30") ➞ "30"

### Notes

  * Return a **string**.
  * If you get a number with `.0` on the end, return the _integer value_ (e.g. return `"4"` rather than `"4.0"`).
  * If the number is `0`, `0.0`, `000`, `00.00`, etc... return `"0"`.

"""

def remove_leading_trailing(n):
    if "." in n:
        natural,decimal=n.split(sep='.')
    else:
        natural=n
        decimal=''
    while len(natural)>1 and natural[0]=='0':
        natural=natural[1:]
    while len(decimal)>=1 and decimal[-1]=='0':
        decimal=decimal[:-1]
    if not len(decimal) :
        return natural
    else:
        return natural+'.'+decimal

