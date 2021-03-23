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

def partially_hide(phrase):
  return ' '.join([word[0] + ''.join(['-' for i in word[1:-1]]) + word[-1] for word in phrase.split()])

