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
    copy = txt[:]
    high = {}
    for let in txt:
        copy = copy.replace(let, "0", 1)
        if copy.find(let) != -1:
            if let in high.keys():
                if high[let] >= copy.find(let) - txt.find(let):
                    continue
                else:
                    high[let] = copy.find(let) - txt.find(let)
            else:
                high[let] = copy.find(let) - txt.find(let)
​
            txt = txt.replace(let, "1", 1)
    max_value_keys = [key for key in high.keys() if high[key] == max(high.values())]
    return sorted(max_value_keys)

