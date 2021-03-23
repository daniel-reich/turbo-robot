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

def staircase(k):
  
    staircase = []
    reverse = []
    x = 0
    symbol = "#"
    under = "_"
    
​
    if k >= 0:
        
        for x in range(k):
            
            string = ""
            for i in range(k-x):
                string += under
            for x in range(x):
                string += symbol
        
            x += 1
            
            if '#' in string:
                staircase.append(string)
​
        string2 = ""
        for x in range(k):
            string2 += symbol
        staircase.append(string2)
        
        for i in range(len(staircase)-1):
​
            staircase[i] += "\n"
    
        return ''.join(staircase)
    
    elif k < 0:
​
        k *= -1
​
        for x in range(k):
            
            string = ""
            for i in range(k-x):
                string += under
            for x in range(x):
                string += symbol
        
            x += 1
            
            if '#' in string:
                staircase.append(string)
​
        string2 = ""
        for x in range(k):
            string2 += symbol
        staircase.append(string2)
    
    
        for item in staircase:
        
            index = staircase.index(item)
            index += 1 
            index *= -1
            reverse.append(staircase[index])
        
        for i in range(len(reverse)-1):
​
            reverse[i] += "\n"
        
        return ''.join(reverse)

