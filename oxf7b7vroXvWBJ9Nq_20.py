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

def discount(n, txt):
  if not txt:
    return n
  txt = txt.split(', ')
  percentages = [float(i[:-1]) for i in txt if i[-1]=='%']
  discounts = [float(i) for i in txt if i[-1]!='%']
  for i in percentages:
    n*=(1-(i/100))
  for i in discounts:
    n-=i
  return round(n,2)

