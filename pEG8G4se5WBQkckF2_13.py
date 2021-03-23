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

def reverse_sort(txt):
  final = ''
  txt = sorted(txt.split(),key=len)
  lengths = {len(i):[] for i in txt}
  for i in txt:
    lengths[len(i)].append(i)
  for i in reversed(range(min(lengths.keys()),max(lengths.keys())+1)):
    if i in lengths:
      final+=' '.join(sorted(lengths[i],key=lambda x:(x.lower(),txt[::-1].index(x)))[::-1])+' '
  return final[:-1]

