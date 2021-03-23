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
    counter = []
    for b in bills:
        change = b - 5
        if change > 0:
            idx = 0
            while change > 0 and idx < len(counter):
                if counter[idx] <= change:
                    change -= counter[idx]
                    counter = counter[:idx] + counter[idx + 1:]
                else:
                    idx += 1
            if change > 0:
                return False
        counter = sorted(counter + [b], reverse=True)
    return True

