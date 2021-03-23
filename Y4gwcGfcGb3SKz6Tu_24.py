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
    long = 0
    ans = []
    for o in range(97, 123):
        sep = chr(o)
        if txt.count(sep) >= 2:
            txt2 = txt[txt.index(sep):]
            while txt2[-1] != sep:
                txt2 = txt2[:-1]
            l = max([len(_) for _ in txt2.split(sep)])
            if l > long:
                ans = [sep]
                long = l
            elif l == long:
                ans.append(sep)
    return ans

