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

def get_drink_ID(fl, ml):
  a=fl.split()
  b=list(map(lambda x:x[0:3], a))
  b=[i.upper() for i in b]
  return "".join(b)+ml.replace("ml",'')

