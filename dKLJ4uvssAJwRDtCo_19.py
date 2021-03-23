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

products = [
  { 'number': 1, 'price': 100, 'name': 'Orange juice' },
  { 'number': 2, 'price': 200, 'name': 'Soda' },
  { 'number': 3, 'price': 150, 'name': 'Chocolate snack' },
  { 'number': 4, 'price': 250, 'name': 'Cookies' },
  { 'number': 5, 'price': 180, 'name': 'Gummy bears' },
  { 'number': 6, 'price': 500, 'name': 'Condoms' },
  { 'number': 7, 'price': 120, 'name': 'Crackers' },
  { 'number': 8, 'price': 220, 'name': 'Potato chips' },
  { 'number': 9, 'price': 80,  'name': 'Small snack' }
]
​
def vending_machine(products, money, product_number):
    if product_number not in range(1,10):
        return "Enter a valid product number"
    if money<products[product_number-1]['price']:
        return 'Not enough money for this product'
    c=[500, 200, 100, 50, 20, 10]
    change_list=[]
    if products[product_number-1]['price']<money:
        change_total=(money-products[product_number-1]['price'])
        
        while change_total:
            for x in range(len(c)):
                if c[x]>change_total:
                    c[x]=0   
            change_list.append(max(c))
            change_total-=max(c)
            
    return {'product':products[product_number-1]['name'],"change":change_list}

