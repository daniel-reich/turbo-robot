"""


Create a function that takes a string, removes all "special" characters (e.g.
`., !, @, #, $, %, ^, &, \, *, (, )`) and returns the new string. The only
non-alphanumeric characters allowed are dashes `-`, underscores `_` and
spaces.

### Examples

    remove_special_characters("The quick brown fox!") ➞ "The quick brown fox"
    
    remove_special_characters("%fd76$fd(-)6GvKlO.") ➞ "fd76fd-6GvKlO"
    
    remove_special_characters("D0n$c sed 0di0 du1") ➞ "D0nc sed 0di0 du1"

### Notes

N/A

"""

import re
def remove_special_characters(txt):
  pat = re.compile(r'[^\w\-\s]')
  return re.sub(pat,'',txt)

