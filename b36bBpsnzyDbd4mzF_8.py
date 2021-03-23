"""


Create a function that calculates the chance of being an imposter. The formula
for the chances of being an imposter is `100 × (i / p)` where `i` is the
imposter count and `p` is the player count. Make sure to round the value to
the nearest integer and return the value as a percentage.

### Examples

    imposter_formula(1, 10) ➞ "10%"
    
    imposter_formula(2, 5) ➞ "40%"
    
    imposter_formula(1, 8) ➞ "13%"

### Notes

The player limit is `10` and the imposter count can only go up to `3`.

"""

def imposter_formula(i, p):
  x=int(round(100*(i/p),0))
  return str(x)+"%"

