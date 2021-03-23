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
    dict = {}
    lst = []
    product_name = products[product_number - 1].get('name')
    product_price = products[product_number - 1].get('price')
    change = []
    price_difference = money - product_price
    coins = [500, 200, 100, 50, 20, 10]
    change_list = []
    for i in coins:
        while price_difference >= i:
            change_list.append(i)
            price_difference -= i
    if product_number > 0 and product_number < len(products) + 1:
        dict['product'] = product_name
        if money >= product_price:
            dict['change'] = change_list
            return dict
        else:
            return "Not enough money for this product"
    else:
        return "Enter a valid product number"

