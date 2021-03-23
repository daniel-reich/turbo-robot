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
  sub = []
​
  for i in range(len(txt)-1):
    for j in range(i+1, len(txt)):
      if txt[i] == txt[j] and txt[i:j+1].count(txt[i]) == 2:
        sub.append(txt[i:j+1])
​
  longest = max(map(len, sub), default=0)
  return sorted(s[0] for s in sub if len(s) == longest)

