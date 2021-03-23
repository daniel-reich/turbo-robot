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

def generate_result_structure(name,chane_list):
    return { 'product': name, 'change': chane_list }
    
def make_change(remainder,coins):
    """Calculate the coins required to make change equal to amount."""
    counts = [0 for _ in coins]
    result = []
    for index, amount in enumerate(coins):     
        #print("index {0}".format(index))
        #print(remainder // amount)
        counts[index] = remainder // amount
        #remainder %= amount
        remainder -= counts[index] * amount
        #print(remainder)
        for i in range(counts[index]):
            result.append(amount)
        
    #print(result)
    return result
​
def vending_machine(products, money, product_number):
    coins = [500, 200, 100, 50, 20, 10]
    result = []
    
    # assign product price & name and validate the inputs
    filtered_list = [x for x in products if x['number']==product_number]
    if len(filtered_list) != 1 :
        return 'Enter a valid product number'
    price = filtered_list[0]['price']
    if money < price:
        return 'Not enough money for this product'
        
    total_coins_to_return = money - price
    print(total_coins_to_return)
    name = filtered_list[0]['name']
    if total_coins_to_return == 0:
        return generate_result_structure(name,[])
    
    #calculate change
    if total_coins_to_return in coins:
        return generate_result_structure(name,[total_coins_to_return])    
    
    change_result  =make_change(total_coins_to_return,coins)
    return generate_result_structure(name,change_result)

