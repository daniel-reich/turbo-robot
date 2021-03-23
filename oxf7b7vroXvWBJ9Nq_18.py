"""


We all love a little bargain.

Your function will get a price, and a load of discounts. Your job is to write
the function so that it calculates the **maximum possible** discount.

  * The price is a Number.
  * The load of discounts is a string like: `15%, 8, 50%`.
  * So, percentages, with `%`, and amounts, without `%`.
  * You have to think about the order of applying the discounts.
  * Round the output amount to the nearest hundreth.
  * Output a Number.

### Examples

    discount(64, "50%, 50%") ➞ 16
    # Reduce 50% twice.
    
    discount(24, "20, 2") ➞ 2
    # Subtract 20 and 2.
    
    discount(20, "10, 10%") ➞ 8
    # Apply 10% discount first and then subtract 10.

### Notes

N/A

"""

import re
​
def discount(n, txt):
    if not len(txt): return n
    discounts = sorted(txt.split(", "), key=lambda x: x[-1])
    for d in discounts:
        if d[-1] == "%":
            n -= float(d[:-1])/100*n
        else:
            n -= float(d)
    sol = "{:.2f}".format(n)
    return int(sol[:-3]) if sol[-3:] == ".00" else float(re.sub(r"0+$", "", sol))

