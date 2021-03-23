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
  li = list(set([x for x in [char for char in txt] if [char for char in txt].count(x) > 1]))
  out = []
  length = 0
  for i in li:
    subs = txt[txt.find(i):txt.rfind(i)]
    if max(len(j) for j in subs.split(i)) > length:
      length = max(len(j) for j in subs.split(i))
      out.clear()
      out.append(i)
    elif max(len(j) for j in subs.split(i)) == length:
      out.append(i)
  return sorted(out)

