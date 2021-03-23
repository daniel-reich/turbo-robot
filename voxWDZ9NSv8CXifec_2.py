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
    hand = {v: 0 for v in [5, 10, 20]}
    for bill in bills:
        if bill == 5:
            hand[5] += 1
        elif bill == 10:
            if hand[5] > 0:
                hand[5] -= 1
            else:
                return False
            hand[10] += 1
        else:   # bill = 20
            if hand[5] > 0 and hand[10] > 0:
                hand[5] -= 1
                hand[10] -= 1
            elif hand[5] >= 3:
                hand[5] -= 3
            else:
                return False
            hand[20] += 1
    return True

