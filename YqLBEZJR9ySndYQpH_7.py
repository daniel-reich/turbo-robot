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
    final=[]
    d=[]
    v=abs(n)
    for i in range(1,v+1):
        a=[]
        for j in range(v):
            while(len(a)<(v-i)):
                a.append("_")
                if len(a)==(v-i):
                    break
            while(len(a)<v):
                a.append("#")
                if len(a)==v:
                    break
        #a.append("\n")
        d.append("".join(a))
    if n<0:
        d=d[::-1]
    s=""
    for i in range(len(d)-1):
       s+=d[i]+"\n"
    s+=d[-1]
    return s

