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

def gimme_the_letters(spectrum):
  alphabet = ''.join([chr(i) for i in range(97, 123)])
​
  if spectrum[0].isupper():
    alphabet = alphabet.upper()
​
  a, b = alphabet.index(spectrum[0]), alphabet.index(spectrum[-1])
  
  return alphabet[a:b+1]

