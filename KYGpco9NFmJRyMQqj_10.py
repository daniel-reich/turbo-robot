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
  txt1_1=set(txt1)
  txt2_2=set(txt2)
  return len(txt1_1^txt2_2)
