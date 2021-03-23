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
  txt_dict = {}
  for i, v in enumerate(txt):
    if v in txt_dict:
      txt_dict[v].append(i)
    else:
      txt_dict[v] = [i]
  diff_dict = {}
  for k, v in txt_dict.items():
    if len(v) > 1:
      diff_dict[k] = max([v[i+1] - v[i] for i, x in enumerate(v) if i != len(v) - 1])
  if diff_dict:
    max_v = max(diff_dict.values())
    return sorted([k for k, v in diff_dict.items() if v == max_v])
  else:
    return []

