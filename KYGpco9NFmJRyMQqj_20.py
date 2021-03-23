"""


Create a function that returns the **smallest number of letter removals** so
that two strings are **anagrams** of each other.

### Examples

    min_removals("abcde", "cab") ➞ 2
    # Remove "d", "e" to make "abc" and "cab".
    
    min_removals("deafk", "kfeap") ➞ 2
    # Remove "d" and "p" from the first and second word, respectively.
    
    min_removals("acb", "ghi") ➞ 6
    # Remove all letters from both words to get "" and "".

### Notes

  * An anagram is any string that can be formed by shuffling the characters of the original string. For example: `baedc` is an anagram of `abcde`.
  * An empty string can be considered an anagram of itself.
  * Characters won't be used more than once per string.

"""

def min_removals(txt1, txt2):
  
  in_both = []
  
  for l8r in txt1:
    if l8r in txt2:
      in_both.append(l8r)
​
  
  inboth_count = len(in_both)
  txt1count = len(txt1)
  txt2count = len(txt2)
  
  if inboth_count == 0:
    removals = txt1count + txt2count
  else:
    removals = (txt1count - inboth_count) + (txt2count - inboth_count)
  
  return removals

