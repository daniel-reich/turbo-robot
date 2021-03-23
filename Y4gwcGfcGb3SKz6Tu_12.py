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

def findall(src, c):
  res, s = [], 0
  while True:
    i = src.find(c, s)
    if i < 0:
      return res
    else:
      res.append(i)
      s = i + 1
​
def max_pairwise_dif(lst):
  p = [i2 - i1 for i1, i2 in zip(lst, lst[1:])]
  return max(p, default=0)
  
def max_separator(string):
  sstr = [(c, max_pairwise_dif(findall(string, c))) for c in set(string)]
  opt_len = max(sstr, key=lambda t: t[1])[1]
  if not opt_len:
    return []
  return list(sorted(t[0] for t in sstr if t[1] >= opt_len))

