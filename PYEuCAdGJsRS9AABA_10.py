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
    def __init__(self, name, menu, orders):
        self.name = name
        self.menu = menu
        self.orders = orders
        self.total = 0
        self.min_item_price = 9999.99
        self.min_item_name = ''
        self.drinks = []
        self.food = []
​
    def add_order(self, item):
        self.item = item
        for x in self.menu:
            if x['item'] == self.item:
                self.orders.append(self.item)
                self.total += x['price']
                return "Order added!"
        return "This item is currently unavailable!"
        
    def fulfill_order(self):
        if len(self.orders) > 0:
            var = self.orders[0]
            del self.orders[0]
            return "The {} is ready!".format(var)
        else:
            self.total = 0
            return "All orders have been fulfilled!"
​
    def list_orders(self):
        return self.orders
​
    def due_amount(self):
        return round(self.total, 2)
​
    def cheapest_item(self):
        for x in self.menu:
            if x['price'] < self.min_item_price:
                self.min_item_price = x['price']
                self.min_item_name = x['item']
        return self.min_item_name
​
    def drinks_only(self):
        for x in self.menu:
            if x['type'] == 'drink':
                self.drinks.append(x['item'])
        return self.drinks
​
    def food_only(self):
        for x in self.menu:
            if x['type'] == 'food':
                self.food.append(x['item'])
        return self.food

