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

def ini(name):
  pos = name.find(' ')
  return name[0] + '. ' + name[pos+1] + '.' 
​
def initialize(names):
  return [ini(name) for name in names]

