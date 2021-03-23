"""


![Pizza Points](https://s3.amazonaws.com/edabit-images/pizza-points.gif)

Google is launching a network of autonomous pizza delivery drones and wants
you to create a flexible rewards system (Pizza Points™) that can be tweaked in
the future. The rules are simple: if a customer has made at least _N_ orders
of at least _Y_ price, they get a FREE pizza!

Create a function that takes a dictionary of customers, a minimum number of
orders and a minimum order price. Return a list of customers that are eligible
for a free pizza.

### Examples

    customers = {
      "Batman": [22, 30, 11, 17, 15, 52, 27, 12],
      "Spider-Man": [5, 17, 30, 33, 40, 22, 26, 10, 11, 45]
    }
    
      pizza_points(customers, 5, 20) ➞ ["Spider-Man"]
    
      pizza_points(customers, 3, 10) ➞ ["Batman", "Spider-Man"]
    
      pizza_points(customers, 5, 100) ➞ []

### Notes

⚠️Sort the returned array of customer names in alphabetical order.

"""

def pizza_points(customers, min_orders, min_price): 
    holder = []
​
    for customer, order_price in customers.items():
        orders = 0
        for price in order_price:
            if price >= min_price:
                orders += 1
        if orders >= min_orders:
            holder.append(customer)               
​
    return sorted(holder)
