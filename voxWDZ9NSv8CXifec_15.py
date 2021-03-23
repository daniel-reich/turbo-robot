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
  change = {5:0,10:0}
  for b in bills:
    if b == 5:
      change[5]+=1
    if b == 10:
      if change[5]:
        change[5]-=1
        change[10]+=1
      else:
        return False
    if b == 20:
      if change[5] and change[10]:
        change[5]-=1
        change[10]-=1
      elif change[5] > 2:
        change[5]-=3
      else: 
        return False
  return True

