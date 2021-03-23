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

from collections import Counter
def max_separator(str):
    found, length = [], 0
    for c, r in [cnt for cnt in Counter(str).most_common() if cnt[1] > 1]:
        start = str.find(c, 0)
        for _ in range(r - 1):
            end = str.find(c, start + 1)
            l = 1 + end - start
            if l >= length:
                if l > length: 
                    found = []
                length = l
                found.append(c)
            start = end
    return sorted(found)

