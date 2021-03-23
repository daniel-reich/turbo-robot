"""


Create a class `Smoothie` and do the following:

  * Create an _instance_ attribute called `ingredients`. 
  * Create a `get_cost` method which calculates the total cost of the _ingredients used_ to make the smoothie.
  * Create a `get_price` method which returns the number from `get_cost` **plus** the number from `get_cost` multiplied by **1.5**. Round to **two decimal places**.
  * Create a `get_name` method which gets the ingredients and puts them in **alphabetical order** into a nice descriptive sentence. If there are multiple ingredients, add the word _"Fusion"_ to the end but otherwise, add _"Smoothie"_. Remember to change **"-berries"** to **"-berry"**. See the examples below.

Ingredient| Price  
---|---  
Strawberries| $1.50  
Banana| $0.50  
Mango| $2.50  
Blueberries| $1.00  
Raspberries| $1.00  
Apple| $1.75  
Pineapple| $3.50  
  
### Examples

    s1 = Smoothie(["Banana"])
    
    s1.ingredients ➞ ["Banana"]
    
    s1.get_cost() ➞ "$0.50"
    
    s1.get_price() ➞ "$1.25"
    
    s1.get_name() ➞ "Banana Smoothie"
    s2 = Smoothie(["Raspberries", "Strawberries", "Blueberries"])
    
    s2.ingredients ➞ ["Raspberries", "Strawberries", "Blueberries"]
    
    s2.get_cost() ➞ "$3.50"
    
    s2.get_price() ➞ "$8.75"
    
    s2.get_name() ➞ "Blueberry Raspberry Strawberry Fusion"

### Notes

Feel free to check out the **Resources** tab for a refresher on classes.

"""

class Smoothie:
  prices = {"Strawberries": 1.5, "Banana": .5, "Mango": 2.5, "Blueberries": 1, "Raspberries":1, "Apple": 1.75, "Pineapple": 3.5}
  
  def __init__(self,ingr=list):
    self.ingredients = ingr
    self.tag = "Fusion" if len(ingr) > 1 else "Smoothie"
    self.cost = sum(self.prices.get(fruit) for fruit in self.ingredients)
    
  def get_name(self):
    return " ".join([x[:-3] + "y" if x.endswith("ies") else x for x in sorted(self.ingredients)] + [self.tag])
​
  def get_cost(self):
    return "${:,.2f}".format(self.cost)
​
  def get_price(self):
    return "${:,.2f}".format(self.cost * 2.5)

