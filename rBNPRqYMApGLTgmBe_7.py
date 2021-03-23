"""
Write a function that returns the amount of possible combinations when drawing
the given amount of cards from a deck of cards.

The function must take two inputs: `k` is the amount of cards to draw. `n` the
total amount of cards in the deck.

For example, a poker hand can be described as a 5-combination (`k` = 5) of
cards from a 52 card deck (`n` = 52). The 5 cards of the hand are all
distinct, and the order of cards in the hand does not matter. There are
2,598,960 such combinations.

The amount of combinations should be returned as an integer.

### Examples

    combinations(52, 52) ➞ 1
    
    combinations(5, 52) ➞ 2598960
    
    combinations(10, 52) ➞ 15820024220

### Notes

  * Try solving this natively without any imports.
  * Remember to return result as integer.

"""

def combinations(k, n):
  j=n-k
  a=1
  b=1
  c=1
  while(n>1):
    a*=n
    n-=1
  while(k>1):
    b*=k
    k-=1
  while(j>1):
    c*=j
    j-=1
  return a//(b*c)

