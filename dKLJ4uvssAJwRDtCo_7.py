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

def vending_machine(products, money, num):
  if num not in range(1, 10):
    return "Enter a valid product number"
  name = products[num -1]['name']
  price = products[num -1]['price']
  diff = money - price
  if diff == 0:
    return {"product": name, "change": []}
  if diff < 0:
    return "Not enough money for this product"
​
  coins = [500, 200, 100, 50, 20, 10]
  change = []
  for coin in coins:
    if diff > 0:
      times = diff // coin
      diff -= times * coin
      change.append(times * [coin])
  change = [i for lst in change for i in lst]
  return {"product": name, "change": change}

