"""


Write a **class** called **CoffeeShop** , which has **three instance
variables** :

  1.  **name** : a string (basically, of the shop)
  2.  **menu** : a list of items (of dict type), with each item containing the **item** (name of the item), **type** (whether a _food_ or a _drink_ ) and **price**.
  3.  **orders** : an empty list

and **seven methods** :

  1.  **add_order** : adds the **name** of the item to the end of the **orders** list if it exists on the **menu** , otherwise, return `"This item is currently unavailable!"`
  2.  **fulfill_order** : if the **orders** list is **not empty** , return `"The {item} is ready!"`. If the **orders** list is empty, return `"All orders have been fulfilled!"`
  3.  **list_orders** : returns the _item_ **names** of the **orders** taken, otherwise, an **empty** list.
  4.  **due_amount** : returns the total amount due for the **orders** taken.
  5.  **cheapest_item** : returns the **name** of the cheapest item on the menu.
  6.  **drinks_only** : returns only the _item_ **names** of _type_ **drink** from the menu.
  7.  **food_only** : returns only the _item_ **names** of _type_ **food** from the menu.

 **IMPORTANT** : Orders are fulfilled in a **FIFO** (first-in, first-out)
order.

### Examples

    tcs.add_order("hot cocoa") ➞ "This item is currently unavailable!"
    # Tesha's coffee shop does not sell hot cocoa
    tcs.add_order("iced tea") ➞ "This item is currently unavailable!"
    # specifying the variant of "iced tea" will help the process
    
    tcs.add_order("cinnamon roll") ➞  "Order added!"
    tcs.add_order("iced coffee") ➞ "Order added!"
    tcs.list_orders ➞ ["cinnamon roll", "iced coffee"]
    # all items of the current order
    
    tcs.due_amount() ➞ 2.17
    
    tcs.fulfill_order() ➞ "The cinnamon roll is ready!"
    tcs.fulfill_order() ➞ "The iced coffee is ready!"
    tcs.fulfill_order() ➞ "All orders have been fulfilled!"
    # all orders have been presumably served
    
    tcs.list_orders() ➞ []
    # an empty list is returned if all orders have been exhausted
    
    tcs.due_amount() ➞ 0.0
    # no new orders taken, expect a zero payable
    
    tcs.cheapest_item() ➞ "lemonade"
    tcs.drinks_only() ➞ ["orange juice", "lemonade", "cranberry juice", "pineapple juice", "lemon iced tea", "vanilla chai latte", "hot chocolate", "iced coffee"]
    tcs.food_only() ➞ ["tuna sandwich", "ham and cheese sandwich", "bacon and egg", "steak", "hamburger", "cinnamon roll"]

### Notes

Round off **due amount** up to **two decimal** places.

"""

class CoffeeShop:
​
    def __init__(self, name, menu, list=[]):
        self.name = name
        self.menu = menu
        self.orders = list
​
​
​
​
    def add_order(self, other):
        listname = []
​
        d = "This item is currently unavailable!"
        for dictionary in self.menu:
            listname.append(dictionary["item"])
        if other in listname:
            d = 'Order added!'
            self.orders.append(other)
        return d
​
​
    def list_orders(self):
        return self.orders
​
​
​
    def fulfill_order(self):
        if self.orders:
            c = self.orders.pop(0)
            return "The {} is ready!".format(c)
        else:
            return "All orders have been fulfilled!"
​
​
    def due_amount(self):
        due = 0
        for dict2 in self.menu:
            if dict2['item'] in self.orders:
                due += dict2['price']
        return round(due, 2)
​
​
    def cheapest_item(self):
        pricelist = []
        for dict2 in self.menu:
            pricelist.append(dict2["price"])
        a = min(pricelist)
        for dict2 in self.menu:
            if dict2["price"] == a:
                cheap = dict2["item"]
        return cheap
​
​
    def food_only(self):
        listfood = []
        for dict0 in self.menu:
            if dict0['type'] == "food":
                listfood.append(dict0['item'])
        return listfood
​
​
    def drinks_only(self):
        drinks = []
        for dict3 in self.menu:
            if dict3["type"] == "drink":
                drinks.append(dict3['item'])
        return drinks

