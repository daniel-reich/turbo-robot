"""


In the trading card game _Magic: the Gathering_ , players must use a resource
called **mana** to cast spells. There are six types of mana in _Magic_ : white
(W), blue (U), black (B), red (R), green (G), and colorless (C). The **mana
cost** of a spell indicates the amount and type(s) of mana that must be paid
to cast the spell.

  * If the mana cost contains a number (such as "3"), that number must be paid with that total amount of mana in _any combination_ of types.
  * If the mana cost contains a mana type ("W", "U", "B", "R", "G", or "C"), that symbol must be paid with one mana of the corresponding type.

Each individual mana in the player's mana pool can only pay one part of the
cost. For example, the mana cost "3WW" requires two white (W) mana and 3
_additional_ mana in any combination of types. The two white mana used to pay
the "WW" do not also contribute to the "3".

In this challenge, the player's mana pool will be represented as a string,
with each character (W, U, B, R, G, or C) representing a single mana. The mana
cost to be paid will also be represented as a string, which may contain a
single one or two digit number and/or any number of W, U, B, R, G, and C
characters.

Write a function that takes in the two strings, the player's mana and a mana
cost, and determines whether or not the player's mana can pay the cost.

### Examples

    can_pay_cost("WWGGR", "2WWG") ➞ True
    
    can_pay_cost("WWGG", "2WWG") ➞ False
    # Not enough total mana.
    
    can_pay_cost("WGGGR", "2WWG") ➞ False
    # Not enough W mana.
    
    can_pay_cost("WUUUBC", "UUB") ➞ True
    # Having extra mana is okay.

### Notes

  * All letters will be uppercase.
  * If there is a number in the mana cost, it will always come at the beginning.
  * An empty mana pool will be represented by an empty string.
  * The function should correctly handle double-digit numbers in the mana cost, as well as a mana cost of "0".

"""

def can_pay_cost(mana_pool, cost):
  if cost.isdigit():
    return len(mana_pool) >= int(cost)
  if not cost.isalpha():
    for i,c in enumerate(cost):
      if not c.isdigit():
        if len(mana_pool) < int(cost[:i]) + len(cost)-i:
          return False
        break
  if any([mana_pool.count(c) < cost.count(c) for c in 'WUBRGC']):
    return False
  return True
