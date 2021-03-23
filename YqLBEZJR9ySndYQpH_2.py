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

staircase=lambda n,k=1:'#'*k if n==k else'_'*(n-k)+'#'*k+'\n'+staircase(n,k+1)if n>0else'_'*(k-1)+'#'if n==-k else'_'*(k-1)+'#'*(-n-k+1)+'\n'+staircase(n,k+1)

