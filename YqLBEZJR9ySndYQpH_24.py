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
  stairList = []
  if n < 0:
    usNum, hashNum, stairs = 0, (n * -1), (n * -1)
  else:
    usNum, hashNum, stairs = (n - 1), 1, n
​
  for i in range(stairs):
    for i in range(usNum):
      stairList.append("_")
    for i in range(hashNum):
      stairList.append("#")
    stairList.append("\n")
    if n < 0:
      usNum += 1
      hashNum -= 1
    else:
      usNum -= 1
      hashNum += 1
​
  stairList.pop()
  stairStr = "".join(stairList)
  return(stairStr)

