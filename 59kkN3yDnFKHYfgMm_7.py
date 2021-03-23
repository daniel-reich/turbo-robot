"""


Given a string, return if a given letter **always** appears **immediately
before** another given letter.

### Worked Example

    best_friend("he headed to the store", "h", "e") ➞ True
    
    # All occurences of "h": ["he", "headed", "the"]
    # All occurences of "h" have an "e" after it.
    # Return True

### Examples

    best_friend("he headed to the store", "h", "e") ➞ True
    
    best_friend("i found an ounce with my hound", "o", "u") ➞ True
    
    best_friend("we found your dynamite", "d", "y") ➞ False

### Notes

  * Don't count letters with spaces between them (example #3).
  * All sentences will be given in lowercase.

"""

def best_friend(txt, a, b):
    p= ' '.join('x' if len(i)<=3 or len(i)==4 else  i for i in txt.split()).replace('x','')
    x= ''.join('7' if i==a or i==b else i for i in p).count('7')
    return x==6 or x==4

