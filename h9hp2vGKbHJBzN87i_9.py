"""


Create a function that takes a phrase and transforms each word using the
following rules:

  1. Keep first and last character the same.
  2. Transform middle characters into a dash `-`.

### Examples

    partially_hide("skies were pretty") ➞ "s---s w--e p----y"
    
    partially_hide("red is not my color") ➞ "r-d is n-t my c---r"
    
    partially_hide("She rolled her eyes") ➞ "S-e r----d h-r e--s"
    
    partially_hide("Harry went to fight the basilisk") ➞ "H---y w--t to f---t t-e b------k"

### Notes

Words with two or fewer letters should not be hidden at all.

"""

partially_hide=lambda t:' '.join(x[0]+'-'*(len(x)-2)+x[-1]if len(x)>2else x for x in t.split())
