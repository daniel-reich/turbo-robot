"""


Given two strings, that may or may not be of the same length, determine the
minimum number of character deletions required to make an anagram. Any
characters can be deleted from either of the strings.

### Examples

    make_anagram("cde", "abc") ➞ 4
    # Remove d and e from cde to get c.
    # Remove a and b from abc to get c.
    # It takes 4 deletions to make both strings anagrams.
    
    make_anagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke") ➞ 30
    
    make_anagram("showman", "woman") ➞ 2

### Notes

N/A

"""

from collections import Counter
​
def make_anagram(a, b):
    Ca = Counter(a)
    Cb = Counter(b)
    ans = 0
    for k in range(97, 123):
        c = chr(k)
        ans += abs(Ca.get(c, 0) - Cb.get(c, 0))
    return ans

