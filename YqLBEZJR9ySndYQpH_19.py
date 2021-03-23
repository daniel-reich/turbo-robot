"""


Create a function that will build a staircase using the underscore `_` and
hash `#` symbols. A positive value denotes the staircase's upward direction
and downwards for a negative value.

### Examples

    staircase(3) ➞ "__#\n_##\n###"
    __#
    _##
    ###
    
    staircase(7) ➞ "______#\n_____##\n____###\n___####\n__#####\n_######\n#######"
    ______#
    _____##
    ____###
    ___####
    __#####
    _######
    #######
    
    staircase(2) ➞ "_#\n##"
    _#
    ##
    
    staircase(-8) ➞ "########\n_#######\n__######\n___#####\n____####\n_____###\n______##\n_______#"
    ########
    _#######
    __######
    ___#####
    ____####
    _____###
    ______##
    _______#

### Notes

  * All inputs are either positive or negative values.
  * The string to be returned is adjoined with the newline character (`\n`).
  * A recursive version of this challenge can be found in [here](https://edabit.com/challenge/ntpgCFga2rRzB53QZ).

"""

def staircase(n):
  out = ""
  r = abs(n)
  if n<0:
    r = abs(n)+1
  for x in range(r):
    t = ""
    r_y = abs(n)- (x+1)
    r_h = x+1
    if n<0:
      r_y = abs(n) - x
      r_h = x
    for y in range(r_y):
      t+="_"
    for y in range(r_h):
      t+="#"
    t+="\n"
    out+=t
  if n<0:
    out = reverse(out)
  return out[:-1]
​
​
def reverse(out):
  t=[]
  e=""
  for x in out:
    if x!="\n":
      e+=x
    else:
      e+="\n"
      t.append(e)
      e=""
  e=""
  for x in range(len(t)-1):
    e+=t[(len(t)-1)-x]
  return e

