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

def max_separator(txt):
  mx = 0
  lst = []
  for i in range(len(txt)):
    for j in range(i+1,len(txt)):
      if txt[i]==txt[j]:
        if len(txt[i:j+1])>mx:
          mx = len(txt[i:j+1])
          lst = [txt[i]]
        elif len(txt[i:j+1])==mx:
          lst.append(txt[i])
        break
  return sorted(lst)

