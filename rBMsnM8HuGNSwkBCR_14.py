"""
Create a function that takes a string containing money in dollars and pounds
sterling (seperated by comma) and returns the sum of _dollar bills only_ , as
an integer.

For the input string:

  * Each amount is prefixed by the currency symbol: **$** for dollars and **£** for pounds.
  * Thousands are represented by the suffix **k**.

i.e. $4k = $4,000 and £40k = £40,000

### Examples

    add_bill("d20,p40,p60,d50") ➞ 20 + 50 = 70
    
    add_bill("p30,d20,p60,d150,p360") ➞ 20  + 150 = 170
    
    add_bill("p30,d2k,p60,d200,p360") ➞ 2 * 1000 + 200 = 2200

### Notes

There is at least one dollar bill in string.

"""

def add_bill(money):
   return sum([int(m[1:-1])*1000 if m[0] == "d" and m[-1] == "k" \
   else int(m[1:]) if m[0] == "d" \
   else 0 for m in money.split(",")])

