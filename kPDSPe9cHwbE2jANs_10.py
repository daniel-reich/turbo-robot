"""


The image below shows a sequence of larger and larger houses of cards, with
the total number of cards included for each:

![House of Cards](https://edabit-challenges.s3.amazonaws.com/hcards.png)

Given the tower height `n`, return the number of cards needed to construct a
full house of cards.

### Examples

    cards_needed(3) ➞ 15
    
    cards_needed(4) ➞ 26
    
    cards_needed(0) ➞ 0

### Notes

The height should always be equal or greater than 0. Return `"invalid"` if the
value given doesn't abide by this rule.

"""

def cards_needed(n):
  
  if n < 0:
    return 'invalid'
    
  seq = [0]
  dif = 2
  current_step = 0
​
  while current_step < n and current_step < 1000:
    seq.append(seq[-1] + dif)
    dif += 3
    current_step += 1
​
  return seq[-1]

