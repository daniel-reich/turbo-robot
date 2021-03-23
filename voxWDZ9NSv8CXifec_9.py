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
    f, te, tw = 0, 0, 0
    if bills[0] != 5:
        return False
    for i in bills:
        if i == 5:
            f += 1
        elif i == 10:
            te += 1
            f -= 1
        elif i == 20:
            tw += 1
            if f >= 3 and te < 1:
                f -= 3
            else:
                te -= 1
                f -= 1
        if f < 0 or te < 0 or tw < 0:
            return False
    return True

