"""


There has been a masterdata issue which affected the prices of the products.
Check if each product has a valid price (integer or float, and greater than or
equal to zero). Products with a price of 0 are free and count as a valid
price.

The return value should be a Boolean.

### Examples

    has_valid_price({ "product": "Milk", "price": 1.50 }) ➞ True
    
    has_valid_price({ "product": "Cheese", "price": -1 }) ➞ False
    
    has_valid_price({ "product": "Eggs", "price": 0 }) ➞ True
    
    has_valid_price({ "product": "Cereals", "price": "3.0" }) ➞ False
    
    has_valid_price(None) ➞ False

### Notes

Type of the price should be an integer/float. If it's anything else, you
should return `False`.

"""

def has_valid_price(product):
  return False if not product else product and False if "price" not in product.keys() else \
    (isinstance(product["price"], int) or isinstance(product["price"], float)) and product["price"] >= 0

