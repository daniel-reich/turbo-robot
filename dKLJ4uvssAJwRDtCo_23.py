"""


Your task is to create a function that simulates a vending machine.

Given an amount of `money` (in cents **¢** to make it simpler) and a
`product_number`, the vending machine should output the correct product name
and give back the correct amount of change.

The coins used for the change are the following: `[500, 200, 100, 50, 20, 10]`

The return value is a dictionary with 2 properties:

  * `product`: the product name that the user selected.
  * `change`: an array of coins (can be empty, must be sorted in descending order).

### Examples

    vending_machine(products, 200, 7) ➞ { "product": "Crackers", "change": [ 50, 20, 10 ] }
    
    vending_machine(products, 500, 0) ➞ "Enter a valid product number"
    
    vending_machine(products, 90, 1) ➞ "Not enough money for this product"

### Notes

  * The products are fixed and you can find them in the **Tests** tab.
  * If `product_number` is invalid (out of range) you should return the _string_ : "Enter a valid product number".
  * If `money` is not enough to buy a certain product you should return the _string_ : "Not enough money for this product".
  * If there's no change, return an empty array as the `change`.

"""

class Product:
  def __init__(self,number):
    self.product = products[number-1]
  def name(self):
    return self.product["name"]
  def price(self):
    return self.product["price"]
​
​
def vending_machine(products, money, product_number):
  p = Product(product_number)
  if product_number < 1 or product_number > 9:
    return "Enter a valid product number"
  elif p.price() > money:
    return "Not enough money for this product"
  else:
    product = p.name()
    remaining = money - p.price()
    coins = [500,200,100,50,20,10]
    change = []
    for coin in coins:
      if coin <= remaining:
        for k in range(0,remaining//coin):
          change.append(coin) 
          remaining -= coin
    return {'product':product,'change':change}

