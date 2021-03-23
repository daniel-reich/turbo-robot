"""


Given a string indicating a range of letters, return a string which includes
all the letters in that range, _including_ the last letter. Note that if the
range is given in _capital letters_ , return the string in capitals also!

### Examples

    gimme_the_letters("a-z") ➞ "abcdefghijklmnopqrstuvwxyz"
    
    gimme_the_letters("h-o") ➞ "hijklmno"
    
    gimme_the_letters("Q-Z") ➞ "QRSTUVWXYZ"
    
    gimme_the_letters("J-J") ➞ J"

### Notes

  * A _hyphen_ will separate the two letters in the string.
  * You don't need to worry about error handling in this one (i.e. both letters will be the same case and the second letter will always be after the first alphabetically).

"""

def gimme_the_letters(sp):
  return "".join(chr(n) for n in range(ord(sp[0]),ord(sp[-1])+1))

