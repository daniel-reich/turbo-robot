"""


You will be given a list of drinks, with each drink being a dictionary with
two properties: name and price. Create a function that has the `drinks` list
as an argument and return the drinks dictionaries sorted by price in ascending
order.

Assume that the following array of drink objects needs to be sorted:

    drinks = [
      {"name": "lemonade", "price": 50},
      {"name": "lime", "price": 10}
    ]

The output of the sorted drinks object will be:

### Examples

    sort_drinks_by_price(drinks) ➞ [{name: "lime", price: 10}, {name: "lemonade", price: 50}]

### Notes

N/A

"""

def sort_drinks_by_price(drinks):
  
  prices = []
  drink_price = {}
  
  for drink in drinks:
    price = drink['price']
    prices.append(price)
    drink_price[price] = drink
  
  prices = sorted(prices)
  drinks = []
  
  for price in prices:
    drinks.append(drink_price[price])
  
  return drinks

