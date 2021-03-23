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
  new_lst=[]
  for i in names:
    j=i.split()
    k=''
    for name in j:
      k+='{}. '.format(name[0])
    new_lst.append(k)   
  return [i[:-1] for i in new_lst]

