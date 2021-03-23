"""


A fruit juice company tags their fruit juices by concatenating the first
**three letters** of the words in a flavor's name, with its capacity.

Create a function that creates product IDs for different fruit juices.

### Examples

    get_drink_ID("apple", "500ml") ➞ "APP500"
    
    get_drink_ID("pineapple", "45ml") ➞ "PIN45"
    
    get_drink_ID("passion fruit", "750ml") ➞ "PASFRU750"

### Notes

  * Capacity will be given as a string, and will always be given in **ml**.
  * Return the letters in **UPPERCASE**.

"""

def get_drink_ID(flavor, ml):
  words = flavor.split(' ')
  product_name = ''.join(map(lambda w: w[:3], words)).upper()
  
  # assume that ml is always suffixed with 'ml'
  product_cap = ml[:-2]
  
  return product_name + product_cap

