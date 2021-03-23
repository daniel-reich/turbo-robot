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

from heapq import *
def lemonade(bills):
    remain_heap = []
    for bill in bills:
        if bill == 5:
            heappush(remain_heap, bill)
        elif bill == 10:
            heappush(remain_heap, bill)
            if remain_heap[0] == 10 or remain_heap[0] == 20:
                return False
            else:
                heappop(remain_heap)
        elif bill == 20:
             heappush(remain_heap, bill)
             if sum(remain_heap[:-1]) < 15:
                 return False
             elif len(remain_heap) < 3:
                 return False
             elif len(remain_heap) >= 3:
                 pop_price_1 = heappop(remain_heap)
                 if pop_price_1 > 15:
                     return False
                 elif pop_price_1 <= 15:
                      pop_price_2 = heappop(remain_heap)
                      if pop_price_1 + pop_price_2 > 15:
                          return False
                      else:
                          pop_price_3 = heappop(remain_heap)
                          if pop_price_1 + pop_price_2 + pop_price_3> 35:
                              return False
​
    return True

