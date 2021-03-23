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
    res = []
    for c in set(s):
        s1 = s[:]
        while s1.count(c) > 1:
            start = s1.find(c)
            s1 = s1[start + 1:]
            len_sub = s1.find(c) + 2
            res.append((len_sub, c))
    if res:
        res.sort(key=lambda t: (-t[0], t[1]))
        max_len = res[0][0]
        return [t[1] for t in res if t[0] == max_len]
    return []

