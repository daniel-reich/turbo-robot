"""


Create a function that takes a string and returns a string with spaces in
between all of the characters.

### Examples

    space_me_out("space") ➞ "s p a c e"
    
    space_me_out("far out") ➞ "f a r  o u t"
    
    space_me_out("elongated musk") ➞ "e l o n g a t e d   m u s k"

### Notes

Treat a space as its own character (i.e. leave three spaces between words).

"""

def space_me_out(s):
  return(s.replace("", " ")[1: -1])

