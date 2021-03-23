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

global order_num
order_num = 1
​
class Pizza:
    def __init__(self,lst):
        global order_num
        self.order_number = order_num
        order_num += 1
        self.ingredients = lst
​
    @classmethod
    def garden_feast(self):
        return self(['spinach', 'olives', 'mushroom'])
    @classmethod
    def hawaiian(self):
        return self(['ham', 'pineapple'])
    @classmethod
    def meat_festival(self):
        return self(['beef', 'meatball', 'bacon'])

