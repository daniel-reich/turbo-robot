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
​
  class Stand:
​
    def __init__(self, price):
      self.p = price
      self.bills = []
    
    def buy(self, bill):
      if bill < self.p:
        return False
      elif bill == self.p:
        self.bills.append(bill)
        return True
      else:
        change = bill - self.p
        possible_payments = []
​
        if change == 5:
          possible_payments = [[5]]
        elif change == 10:
          possible_payments = [[5, 5], [10]]
        else:
          possible_payments = [[5, 5, 5], [10, 5]]
        
        for possability in possible_payments:
          valid = True
          for bll in set(possability):
            if bll not in self.bills:
              valid = False
              break
            bill_count = self.bills.count(bll)
            poss_count = possability.count(bll)
​
            if bill_count < poss_count:
              valid = False
              break
          if valid == True:
            for bll in possability:
              try:
                self.bills.pop(self.bills.index(bll))
              except ValueError:
                return possability, self.bills, change
            self.bills.append(bill)
            return True
        self.bills.append(bill)
        return False
​
  stand = Stand(5)
​
  for bill in bills:
    purchase = stand.buy(bill)
   # print(stand.bills)
    if purchase == False:
      return False
    elif isinstance(purchase, bool) == False:
      return purchase
  
  return True

