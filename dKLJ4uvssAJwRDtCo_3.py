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

def vending_machine(products, money, product_number):
  if product_number not in range(1, len(products)+1):
    return "Enter a valid product number"
  product = products[product_number-1]
  owed = money - product['price']
  if owed < 0:
    return "Not enough money for this product"
  coins = []
  denoms = [500, 200, 100, 50, 20, 10]
  i = 0
  while owed > 0:
    while owed < denoms[i]:
      i += 1
    coins.append(denoms[i])
    owed -= denoms[i]
  return {'change' : coins, 'product' : product['name']}

