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

prices = {
  "Strawberries" : "$1.50",
  "Banana" : "$0.50",
  "Mango" : "$2.50",
  "Blueberries" : "$1.00",
  "Raspberries" : "$1.00",
  "Apple" : "$1.75",
  "Pineapple" : "$3.50"
}
​
​
class Smoothie:
  def __init__(self, ingredients):
    self.ingredients = ingredients
  
  def get_cost(self):
    cost = sum(
      float(prices[ingredient][1:])
      for ingredient in self.ingredients)
    return '${:.2f}'.format(cost)
  
  def get_price(self):
    cost = float(self.get_cost()[1:])
    price = cost + cost * 1.5
    return '${:.2f}'.format(price)
    
  def get_name(self):
    ingredients = sorted(
      ingredient.replace('berries', 'berry')
      for ingredient in self.ingredients)
    smoothie_type = 'Fusion' if len(self.ingredients) > 1 else 'Smoothie'
    return '{} {}'.format(' '.join(ingredients), smoothie_type)

