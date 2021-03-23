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

def max_separator(s):
  a = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)] 
  b = sorted([x for x in a if x[0] == x[-1] and len(x) >= 2])
  c = sorted([x for x in b if x[0] not in x[1:-1]],key=len)
  res = [x for x in c if len(x) == max(len(x) for x in c)]
  return [i[0] for i in res]

