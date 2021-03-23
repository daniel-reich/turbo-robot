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
    change = [500, 200, 100, 50, 20, 10]
​
    for x in products:
        if x['number'] == product_number:
            name = x['name']
            price = x['price']
            break
    else:
        return 'Enter a valid product number'
    
    if money < price: return 'Not enough money for this product'
    
    required = money - price
    change_set = []
    while required:
        for i in change:
            if required  >= i:
                change_set.append(i)
                required -= i
                break
    
    return {'product': name, 'change': change_set}

