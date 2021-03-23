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
'Strawberries' : '$1.50',
'Banana' : '$0.50',
'Mango' : '$2.50',
'Blueberries' : '$1.00',
'Raspberries' : '$1.00',
'Apple' : '$1.75',
'Pineapple' : '$3.50'
}
​
class Smoothie:
    def __init__(self, ingredients):
        self.ingredients = ingredients
​
    def get_cost(self):
        # return the cost if it
        # was already calculated
        try:
            return self.cost
​
        except:
            # get the ingredients and their costs
            ingredients = self.ingredients
​
            # sum the costs
            totalCost = 0
​
            for ingredient in ingredients:
                # strip '$' and convert to float
                cost = prices[ingredient][1:]
                totalCost += float(cost)
​
            # format cost as string
            totalCost = '${0:.2f}'.format(totalCost)
​
            # create new attribute and return
            self.cost = totalCost
            return totalCost
​
    def get_price(self):
        try:
            return self.price
​
        except:
            try:
                cost = self.cost
​
            except:
                # calculate the cost
                cost = self.get_cost()
​
            # strip '$' and convert to float
            cost = float(cost[1:])
​
            # calculate the price
            price = 2.5 * cost
​
            # format price as string
            price = '${0:.2f}'.format(price)
​
            self.price = price
            return price
​
    def get_name(self):
        try:
            return self.name
​
        except:
            # sort the ingredients alphabetically
            ingredients = sorted(self.ingredients)
​
            # replace all -ies with -y
            # then join list into string
            for (i, ingredient) in enumerate(ingredients):
                ingredients[i] = ingredient.replace('ies', 'y')
​
            name = ' '.join(ingredients)
​
            # add the name suffix
            if len(ingredients) > 1:
                name += ' Fusion'
​
            else:
                name += ' Smoothie'
​
            self.name = name
            return name

