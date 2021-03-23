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

def max_separator(string):
  def find_substrings(s):
    substrings = {}
    l8rs = list(set(s))
   # print(l8rs)
    for l8r in l8rs:
      count = s.count(l8r)
      indexes = []
    #  print(l8r, count)
      for n in range(len(s)):
        if s[n] == l8r:
          indexes.append(n)
     # print(indexes)
      substrings[l8r] = [indexes[n+1] - indexes[n] for n in range(len(indexes)-1)]
    
    return substrings
  
  fs = find_substrings(string)
​
  max_substring = 0
  max_l8r = []
​
  for l8r in fs:
    try:
      if max(fs[l8r]) > max_substring:
        max_substring = max(fs[l8r])
        max_l8r = [l8r]
      elif max(fs[l8r]) == max_substring:
        max_l8r.append(l8r)
    except ValueError:
      continue
​
  return sorted(max_l8r)

