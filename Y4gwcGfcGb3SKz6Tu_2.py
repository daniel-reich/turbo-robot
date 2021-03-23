"""


Given a string of letters, create a function that returns a list with the
separator that yields the longest possible substring, provided that:

  * The substring starts and ends with the separator.
  * The separator doesn't occur inside the substring other than at the ends.

If two or more separators yield substrings with the same length, they should
appear in alphabetical order.

### Examples

    max_separator("supercalifragilistic") ➞ ["s"]
    # The longest substring is "supercalifragilis".
    
    max_separator("laboratory") ➞ ["a", "o", "r"]
    # "abora", "orato" and "rator" are the same length.
    
    max_separator("candle") ➞ []
    # No possible substrings.

### Notes

  * All substrings should be at least of length 2 (i.e. no single-letter substrings).
  * Expect lowercase alphabetic characters only.

"""

import re
def max_separator(txt):
  al = 'abcdefghijklmnopqrstuvwxyz'
  M = max(max([0]+[len(m) for m in re.findall('{}[^{}]*(?={})'.format(l,l,l),txt)]) for l in al)
  if M==0: return []
  return [l for l in al if max([0]+[len(m) for m in re.findall('{}[^{}]*(?={})'.format(l,l,l),txt)])==M]

