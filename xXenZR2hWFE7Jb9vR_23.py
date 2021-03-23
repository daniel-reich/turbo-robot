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

def is_isomorphic(s, t):
  A=[x for x in zip(s,t)]
  B=[]
  for x in A:
    if not B or not any(x[0]==y[0] for y in B):
      B.append(x)
  C=[x[::-1] for x in B]
  d1=dict(B)
  d2=dict(C)
  res1=''
  for x in s:
    res1+=d1[x]
  res2=''
  for x in t:
    res2+=d2[x]
  return res1==t and res2==s

