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
class Smoothie:
    ingredientlist = []
    cost = 0
    taxcost = 0
    strcost = ''
    finalsentence = ''
    
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.ingredientlist = ingredients
    
    def get_cost(self):
        for i in range(0, len(self.ingredientlist)):
            self.cost = self.cost + float(prices[self.ingredientlist[i]][1 : ])
        self.strcost = str(self.cost * 1.5)
        return "${:,.2f}".format(self.cost)
        
    def get_price(self):
        if str(self.cost * 1.5)[-2] != '.' and str(self.cost * 1.5)[-3] != '.' and str(self.cost * 1.5)[list(str(self.cost * 1.5)).index('.') + 3] == '5':
            self.cost = self.cost + round((self.cost * 1.5) + 0.001, 2)
        else:
            self.cost = self.cost + round(self.cost * 1.5, 2)
        return "${:,.2f}".format(self.cost)
        
    def get_name(self):
        self.ingredientlist.sort()
​
        for i in range(0, len(self.ingredientlist)):
            if self.ingredientlist[i] == "Blueberries":
                self.finalsentence = self.finalsentence + "Blueberry "
            elif self.ingredientlist[i] == "Raspberries":
                self.finalsentence = self.finalsentence + "Raspberry "
            elif self.ingredientlist[i] == "Strawberries":
                self.finalsentence = self.finalsentence + "Strawberry "
            else:
                self.finalsentence = self.finalsentence + self.ingredientlist[i] + ' '
        if len(self.ingredientlist) == 1:
            self.finalsentence = self.finalsentence + "Smoothie"
        else:
            self.finalsentence = self.finalsentence + "Fusion"
        return self.finalsentence

