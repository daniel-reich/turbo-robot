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
  money = [0,0]
  for b in bills:
    if b == 5:
      money[0] += 1
    elif b == 10:
      money[1] += 1
      if money[0]:
        money[0] -= 1
      else:
        return False
    elif b == 20:
      if money[1] and money[0]:
        money[1] -= 1
        money[0] -= 1
      elif money[0] >= 3:
        money[0] -= 3
      else:
        return False
  return True

