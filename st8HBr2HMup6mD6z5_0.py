"""


Create a function that calculates the profit margin given `cost_price` and
`sales_price`. Return the result as a percentage formated string, and rounded
to one decimals. To calculate profit margin you subtract the cost from the
sales price, then divide by salesprice.

### Examples

    profit_margin(50, 50) ➞ "0.0%"
    
    profit_margin(28, 39) ➞ "28.2%"
    
    profit_margin(33, 84) ➞ "60.7%"

### Notes

  * Remember to return the result as a percentage formated string.
  * Only one decimal should be included.

"""

def profit_margin(cost_price, sales_price):
  return '{:.1%}'.format((sales_price - cost_price)/sales_price)

