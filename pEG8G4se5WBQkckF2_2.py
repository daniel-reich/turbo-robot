"""


Write a function that **sorts the words** in a given string
**lexicographically** (lexical sort) and by **length** in **reverse** order.

### Examples

    reverse_sort("You've rocked the pragmatic world in the making!") 
     ➞ "pragmatic making! You've rocked world the the in"
    
    reverse_sort("Tesh makes my world worth enjoying and living for.")
     ➞ "enjoying living worth world makes Tesh for. and my"
    
    reverse_sort(reverseSort("Shaken by the bloody truth and crazy lies.")
     ➞ "Shaken bloody truth lies. crazy the and by"
    
    reverse_sort("Programming in Python is a lot of fun.")
     ➞ "Programming Python fun. lot of is in a"

### Notes

  * Special characters, punctuations and symbols are part of the word that directly preceeds it.
  * The **space character** separates each word in the given string.
  * Case **insensitive** sorting is required.

"""

def reverse_sort(s):
  r, s = [], sorted(s.split(), key=len)[::-1]
  while len(s):
    if len(r) and len(r[-1][-1]) == len(s[0]): r[-1] += [s[0]]
    else: r += [[s[0]]]
    s = s[1:]
  return ' '.join([' '.join(reversed(sorted(x, key=str.casefold))) for x in r])

