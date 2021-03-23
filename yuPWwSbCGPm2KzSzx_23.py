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
​
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.prices = {
            "Strawberries" : "$1.50",
            "Banana" : "$0.50",
            "Mango" : "$2.50",
            "Blueberries" : "$1.00",
            "Raspberries" : "$1.00",
            "Apple" : "$1.75",
            "Pineapple" : "$3.50"}
​
    def sorted(self):
        self.ingredients1 = list(set(self.ingredients))
        self.ingredients1.sort()
        return self.ingredients1
​
    def change_name(self):
        for i,j in enumerate(self.sorted()):
            if j[-7:] == 'berries':
                self.ingredients1[i] = j.split('berries')[0]+'berry'
        return self.ingredients1
​
    def get_cost(self):
        sum = 0
        for item in self.sorted():
            if item in self.prices.keys():
                sum += float(self.prices.get(item)[1:])
        return "{}{:.2f}".format("$",sum)
​
    def get_price(self):
        return "{}{:.2f}".format("$",float(self.get_cost()[1:]) * (1.0 + 1.5))
​
    def get_name(self):
        if len(self.change_name()) > 1:
            n1 = ""
            for n in self.change_name():
                n1 += n+" "
            return n1 + "Fusion"
        elif len(self.change_name()) == 1:
            return "{} Smoothie".format(self.change_name()[0])
        else:
            return None

