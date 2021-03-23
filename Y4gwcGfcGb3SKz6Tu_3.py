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
    lst, length = [], 2
    for i in range(len(s)-1):
        for j in range(i,len(s)):
            if s[i] == s[j] and s[i:j+1].count(s[i]) == 2:
                if j-i+1 == length:
                    lst.append(s[i])
                elif j-i+1 > length:
                    length = j-i+1
                    lst = [s[i]]
    return sorted(lst)

