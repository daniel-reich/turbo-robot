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
  
  
  d = {'B':0,'W':0,'R':0,'G':0,'U':0,'C':0}
  e = {'B':0,'W':0,'R':0,'G':0,'U':0,'C':0}
  total = 0
  for i in range(0,len(mana_pool)):
    d[mana_pool[i]]+=1
      
  variable = 0
  i = 0
  while i<len(cost):
    if ord(cost[i])>57:
      e[cost[i]]+=1
      i+=1
    else:
      tmp = ""
      j = i
      val=-1
      while j<len(cost):
        if ord(cost[j])>57:
          val = j
          break
        else:
          tmp+=cost[j]
          j+=1
      variable+=int(tmp)
      if val>0:
        i = val
      else:
        break
      
  
  for x in e:
    if d[x]<e[x]:return False
    d[x]-=e[x]
    total+=d[x]
  return total>=variable

