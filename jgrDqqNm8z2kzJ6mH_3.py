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
    nontaxable = sum(p["prc"]*p["qty"] for p in cart if not p["taxable"])
    taxable = sum(p["prc"]*p["qty"] for p in cart if p["taxable"])
    return taxable*1.06 + nontaxable

