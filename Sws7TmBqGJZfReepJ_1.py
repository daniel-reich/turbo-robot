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

def make_anagram(a, b):
    if len(a)>len(b):       
        large = sorted(a)
        small = sorted(b)
    else:
        large = sorted(b)
        small = sorted(a)
    res=[]                      
    for i in range(len(large)):
        if large[i] in small:
            small.remove(large[i])
            res.append(large[i])
    return ((len(large)-len(res))+len(small))

