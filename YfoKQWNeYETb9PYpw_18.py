"""


You work for a manufacturer, and have been asked to calculate the total profit
made on the sales of a product. You are given a dictionary containing the
_cost price per unit_ (in dollars), _sell price per unit_ (in dollars), and
the _starting inventory_. Return the total **profit** made, rounded to the
nearest dollar.

### Examples

    profit({
      "cost_price": 32.67,
      "sell_price": 45.00,
      "inventory": 1200
    }) ➞ 14796
    
    profit({
      "cost_price": 225.89,
      "sell_price": 550.00,
      "inventory": 100
    }) ➞ 32411
    
    profit({
      "cost_price": 2.77,
      "sell_price": 7.95,
      "inventory": 8500
    }) ➞ 44030

### Notes

  * Assume all inventory has been sold.
  * Profit = Total Sales - Total Cost

"""

def profit(info):
  p=info.get('inventory')*(info.get('sell_price')-info.get('cost_price'))
  return round(p)

