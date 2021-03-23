"""


A strong Scottish accent makes every vowel similar to an "e", so you should
replace every vowel with an "e". Additionally, it is being screamed, so it
should be in block capitals.

Create a function that takes a string and returns a string.

### Examples

    to_scottish_screaming("hello world") ➞ "HELLE WERLD"
    
    to_scottish_screaming("Mr. Fox was very naughty") ➞ "MR. FEX WES VERY NEEGHTY"
    
    to_scottish_screaming("Butterflies are beautiful!") ➞ "BETTERFLEES ERE BEEETEFEL!"

### Notes

  * Make sure to include all punctuation that is in the original string.
  * You don't need any more namespaces than are already given.

"""

from re import sub
​
def to_scottish_screaming(txt):
  return sub('[AIOU]', 'E', txt.upper())

