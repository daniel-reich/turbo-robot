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

def staircase(s):
    g = ''
    r = s
    if str(s)[0] != '-':
        for i in range(1, (s + 1)):
            r -= 1
            if i != s:
                g = g + ('_'*r) + ('#'*i) + '\n'
            else:
                g = g + ('_'*r) + ('#'*i)
        return g
    else:
        s = int(str(s).replace('-', ''))
        r = s
        for i in range(s):
            if i != (s - 1):
                g = g + ('_'*i) + ('#'*r) + '\n'
            else:
                g = g + ('_'*i) + ('#'*r)
            r -= 1
        return g

