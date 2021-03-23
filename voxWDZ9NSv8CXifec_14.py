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
  
  # Variables to Denote 'Till'
  Fives = 0
  Tens = 0
  Twenties = 0
  
  Counter = 0
  Length = len(bills)
  
  while (Counter < Length):
    
    # Filling 'Till' with Note of Payment
    Paying_With = bills[Counter]
    
    if (Paying_With == 5):
      Fives += 1
    elif (Paying_With == 10):
      Tens += 1
    elif (Paying_With == 20):
      Twenties += 1
    else:
      return "ERROR"
    
    # Establishing Change Required
    Change = Paying_With - 5
    
    # Dispensing Change (in theory)
    
    if (Change == 0):
      Counter += 1
    
    else:
      
      while (Change >= 20) and (Twenties > 0):
        Twenties -= 1
        Change -= 20
      
      while (Change >= 10) and (Tens > 0):
        Tens -= 1
        Change -= 10
      
      while (Change > 0):
        Fives -= 1
        Change -= 5
    
      # Testing the 'in theory' part of the above comment
      if (Twenties < 0) or (Tens < 0) or (Fives < 0):
        return False
      else:
        Counter += 1
  
  # If everyone gets their change
  return True

