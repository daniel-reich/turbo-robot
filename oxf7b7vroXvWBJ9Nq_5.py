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

def discount(cost, discounts):
    '''
    Returns price after discounts applied to cost so as to maximise the
    discounts as per the instructions
    '''
    from itertools import permutations
    from functools import reduce
​
    if len(discounts) == 0:
        return round(cost, 2)
    
    uniques = set()
    best = cost
    discounts = discounts.split(', ')
    
​
    for combo in permutations(discounts, len(discounts)):
        if combo not in uniques:
            comb_list = [cost] + list(combo)
            price = reduce(lambda a,b: a - float(b) if b[-1] != '%' else \
                           a - float(b[:-1])/100 * a, comb_list)
            uniques.add(combo)
            if price < best:
                best = price
​
    return round(best, 2)

