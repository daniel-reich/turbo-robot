"""


Create a function which takes a list of objects from the class `IceCream` and
returns **the sweetness value of the sweetest icecream**. Note that there is a
class is provided for you in the **Tests tab**.

    class IceCream:
      def __init__(self, flavor, num_sprinkles):
        self.flavor = flavor
        self.num_sprinkles = num_sprinkles

  * Each sprinkle has a _sweetness value of 1_
  * Check below for the sweetness values of the different flavors.

Flavors| Sweetness Value  
---|---  
Plain| 0  
Vanilla| 5  
ChocolateChip| 5  
Strawberry| 10  
Chocolate| 10  
  
### Examples

    ice1 = IceCream("Chocolate", 13)         # value of 23
    ice2 = IceCream("Vanilla", 0)           # value of 5
    ice3 = IceCream("Strawberry", 7)         # value of 17
    ice4 = IceCream("Plain", 18)             # value of 18
    ice5 = IceCream("ChocolateChip", 3)      # value of 8
    sweetest_icecream([ice1, ice2, ice3, ice4, ice5]) ➞ 23
    
    sweetest_icecream([ice3, ice1]) ➞ 23
    
    sweetest_icecream([ice3, ice5]) ➞ 17

### Notes

  * Remember to only return the **sweetness value**.
  * `IceCream` class is provided (check **Tests** tab).

"""

def sweetest_icecream(lst):
  flavours = {"Plain": 0,
        "Vanilla": 5,
        "ChocolateChip": 5,
        "Strawberry": 10,
        "Chocolate": 10
        } 
  
  return max([flavours[ice_cream.flavor] + ice_cream.num_sprinkles for ice_cream in lst])

