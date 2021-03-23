"""


Create a function that takes in a list of full names and returns the initials.

### Examples

    initialize(["Stephen Hawking"]) ➞ ["S. H."]
    
    initialize(["Harry Potter", "Ron Weasley"]) ➞ ["H. P.", "R. W."]
    
    initialize(["Sherlock Holmes", "John Watson", "Irene Adler"]) ➞ ["S. H.", "J. W.", "I. A."]

### Notes

  * Each initial is followed by a dot.
  * Names will always be made of two words, separated by a space.

"""

def initialize(names):
  import re
  bla = [i.lower() for i in names]
  bla = [i.title() for i in bla]
  y = [re.sub(r'([a-z])','', bla[i]) for i in range(len(bla))]
  x = []
  for a in y:
    x.append(re.sub(r'([A-Z])', r'\1.', re.sub(r'[,:=/]', '', a)))
  return x

