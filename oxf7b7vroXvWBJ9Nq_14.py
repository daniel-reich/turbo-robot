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
  def find_possible_discounts(txt):
    discounts = txt.split(', ')
    from itertools import permutations as p
​
    alldiscounts = p(discounts, len(discounts))
​
    return list(alldiscounts)
  def apply_discount(n, discounts):
    def discount(n, dcount):
      if '%' in dcount:
        r = float(dcount[:-1])/ 100
        return n - (n * r)
      else:
        return n - float(dcount)
​
    for item in discounts:
      n = discount(n, item)
    
    return n
      
  if txt == '':
    return n
​
  alldiscounts = find_possible_discounts(txt)
  discounts = []
​
  for sale in alldiscounts:
    discounts.append(abs(apply_discount(n, sale)))
  
  return round(min(discounts),2)

