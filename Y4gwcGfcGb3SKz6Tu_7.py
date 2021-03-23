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
    r = []
    d = sorted([[y, x] for x, y in enumerate(txt)], key=lambda x : x[0])
    last = d[0][0]
    for i in range(1, len(d)):
        if d[i][0] == last:
            add = [d[i][1] - d[i - 1][1], d[i][0]]
            r.append(add)
        last = d[i][0]
    r = sorted(r, key=lambda x : x[0], reverse=True)
    return sorted([y for x, y in r if x == r[0][0]])

