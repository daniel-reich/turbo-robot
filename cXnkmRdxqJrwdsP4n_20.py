"""


Create a function that takes two arguments: the original `price` and the
`discount` percentage as integers and returns the final price after the
discount.

![Alternative Text](https://edabit-
challenges.s3.amazonaws.com/discounts-300x230.jpg)

### Examples

    dis(1500, 50) ➞ 750
    
    dis(89, 20) ➞ 71.2
    
    dis(100, 75) ➞ 25

### Notes

Your answer should be rounded to two decimal places.

"""

def dis(price, discount):
  return round(price - price * discount/100, 2)

