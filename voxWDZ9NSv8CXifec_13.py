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
    bank = []
    for i in bills:
        if i==5:
            bank.append(5)
        elif i==10:
            if 5 in bank:
                bank.append(10)
                bank.remove(5)
            else:
                return False
        else:
            if 5 in bank and 10 in bank:
                bank.append(20)
                bank.remove(5)
                bank.remove(10)
            elif bank.count(5)==3:
                bank.append(20)
                bank = sorted(bank)[3:]
            else:
                return False
    return True

