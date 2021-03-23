"""


Create a function which **replaces** all instances of `"nts"` with `"nce"` and
**vice versa** if they are at the _end of a word_.

### Examples

    switcheroo("The elephants in France were chased by ants!") ➞ "The elephance in Frants were chased by ance!"
    
    switcheroo("While he rants, I fall into a trance...") ➞ "While he rance, I fall into a trants..."
    
    switcheroo("Bounced over the fence!") ➞ "Bounced over the fents!"

### Notes

  * Empty strings should return just an empty string (see example #2).
  * Ignore punctuation and any instances where `"nts"` or `"nce"` are not at the end of a word (see example #3).

"""

import re
def switcheroo(txt):
  print( txt)
  switch_1 = re.sub( r'\Bnts\b', '!!!', txt )
  switch_2 = re.sub( r'\Bnce\b', '???', switch_1 )
  final = switch_2.replace('!!!', 'nce').replace('???','nts')
  return( final)

