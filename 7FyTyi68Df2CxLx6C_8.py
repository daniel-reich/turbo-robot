"""


Create a `Pizza` class with the attributes `order_number` and `ingredients`
(which is given as a list). Only the ingredients will be given as input.

You should also make it so that its possible to choose a ready made pizza
flavour rather than typing out the ingredients manually! As well as creating
this `Pizza` class, hard-code the following pizza flavours.

Name| Ingredients  
---|---  
hawaiian| ham, pineapple  
meat_festival| beef, meatball, bacon  
garden_feast| spinach, olives, mushroom  
  
### Examples

    p1 = Pizza(["bacon", "parmesan", "ham"])    # order 1
    p2 = Pizza.garden_feast()                  # order 2
    p1.ingredients ➞ ["bacon", "parmesan", "ham"]
    
    p2.ingredients ➞ ["spinach", "olives", "mushroom"]
    
    p1.order_number ➞ 1
    
    p2.order_number ➞ 2

### Notes

  * All words are given in lowercase.
  * See the **Resources** tab for some helpful tutorials on classes!

"""

order_number = 0
class Pizza:
  def __init__(self, ingredients):
    global order_number
    self.ingredients = ingredients
    order_number += 1
    self.order_number = order_number 
  def garden_feast():
    a = Pizza(['spinach', 'olives', 'mushroom'])
    return a
  def hawaiian():
    a = Pizza(['ham', 'pineapple'])
    return a
  def meat_festival():
    a = Pizza(['beef', 'meatball', 'bacon'])
    return a

