"""


At a lemonade stand, each lemonade costs $5. Customers are standing in a queue
to buy from you, and order one at a time (in the order specified by `bills`).

Each customer will only buy one lemonade and pay with either a $5, $10, or $20
bill. You must provide the correct change to each customer so that the net
transaction is that the customer pays $5.

Return `True` if and only if you can provide every customer with correct
change.

### Examples

    lemonade([5, 5, 5, 10, 20]) ➞ True
    
    lemonade([5, 5, 10, 10, 20]) ➞ False
    
    lemonade([10, 10]) ➞ False
    
    lemonade([5, 5, 10]) ➞ True

### Notes

  * You don't have any change in hand at first.
  * `bills` is an integer list.
  * `bills[i]` will be either `5`, `10`, or `20`.

"""

def lemonade(bills):
  current_money = [0, 0]
  for bill in bills:
    if bill == 5:
      current_money[0] += 1
    elif bill == 10:
      current_money[0] -= 1
      if current_money[0] < 0: 
        return False
      current_money[1] += 1
    else:
      if current_money[0] > 2: 
        current_money[0] -= 3
      elif current_money[0] > 0 and current_money[1] > 0 : 
        current_money[0] -= 1; current_money[1] -= 1
      else:
        return False
​
  return True

