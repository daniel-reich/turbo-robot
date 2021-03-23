"""


Given two strings `s` and `t`, create a function to determine if they are
isomorphic. Two strings are isomorphic if the characters in `s` can be
replaced to get `t`. All occurrences of a character must be replaced with
another character while preserving the order of characters. No two characters
may map to the same character but a character may map to itself.

### Examples

    is_isomorphic("egg", "add") ➞ True
    
    is_isomorphic("aba", "baa") ➞ False
    
    is_isomorphic("paper", "title") ➞ True

### Notes

N/A

"""

from collections import*
def is_isomorphic(s,t):
  d=defaultdict(set)
  for x,y in zip(s,t):d[x].add(y)
  return all(len(d[x])==1for x in d)and len(d)==len(set(d[x].pop()for x in d))

