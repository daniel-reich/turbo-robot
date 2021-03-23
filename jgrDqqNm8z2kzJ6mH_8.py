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

tax = .06
def checkout(cart):
  
  till = 0
  
  for item in cart:
    item_price = item['prc']
    item_quant = item['qty']
    item_tax = item['taxable']
    
    t = item_price * item_quant
    
    if item_tax == True:
      t += (t * tax)
    
    till += t
  
  return till

