"""


Create a function that takes a list of objects and calculate the total based
on the quantity of items purchased. Apply a 6% sales tax for each item when
appropriate.

### Examples

    checkout([
      { "desc": "potato chips", "prc": 2, "qty": 2, "taxable": false },
      { "desc": "soda", "prc": 3, "qty": 2, "taxable": false },
      { "desc": "paper plates", "prc": 5, "qty": 1, "taxable": true }
    ]) ➞ 15.3

### Notes

N/A

"""

def checkout(cart):
    [total,itotal] = [0,0]
    for item in cart:
        if item["taxable"]:
            itotal = item['prc']*item["qty"]
            itotal+=itotal*0.06
        else:itotal+=item['prc']*item["qty"]
        total +=itotal
        itotal=0
    return total

