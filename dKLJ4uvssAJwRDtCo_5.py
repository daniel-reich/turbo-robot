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
  product_found = False
  coin_list = [500, 200, 100, 50, 20, 10]
  for product in products:
    if product_number == product['number']:
      product_found = True
      product_price = product['price']
      return_dict = {'product': product['name']}
      break
  if not product_found:
    return "Enter a valid product number"
    
  if money < product_price:
    return "Not enough money for this product"
​
  coin_return = []
  remaining_change = money - product_price
  while remaining_change > 0:
    for coin in coin_list:
      if coin <= remaining_change:
        coin_return.append(coin)
        remaining_change -= coin
        break
  
  return_dict['change'] = coin_return
  
  return return_dict

