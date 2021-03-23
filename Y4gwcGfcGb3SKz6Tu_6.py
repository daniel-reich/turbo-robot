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
    test = list(set(txt)); diff_max = []
    for i in test:
        p_i = [k for k, x in enumerate(txt) if x == i]
        if len(p_i) > 1:
            diff = [p_i[n] - p_i[n-1] for n in range(1,len(p_i))]
        else:
            diff = [0]
        diff_max.append(max(diff))
    
    result = [c for c, j in enumerate(diff_max) if j == max(diff_max) != 0]
    return sorted([test[n] for n in result])

