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
  * The string to be returned should be adjoined with the newline character `\n`.
  * You're expected to solve this challenge using a **recursive approach**.
  * You can read more on recursion (see **Resources** tab) if you aren't familiar with it or haven't fully understood the concept before taking this challenge.
  * A non-recursive version of this challenge can be found [here](https://edabit.com/challenge/YqLBEZJR9ySndYQpH).

"""

def staircase(n):
  n_abs = abs(n)
​
  def _make_staircase(step):
    if not step:
      return ""
    yield ("#"*step).rjust(n_abs, '_')
    yield from _make_staircase(step-1)
  
  result = [i for i in _make_staircase(n_abs)]
  return '\n'.join(result if n < 0 else result[::-1])

