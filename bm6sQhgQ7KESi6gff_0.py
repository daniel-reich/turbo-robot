"""


You are given two strings `s` and `t`. String `t` is generated by randomly
shuffling string `s` and then adding one more letter at a random position.
Return the letter that was added to `t`.

### Examples

    find_the_difference("abcd", "abcde") ➞ "e"
    
    find_the_difference("", "y") ➞ "y"
    
    find_the_difference("ae", "aea") ➞ "a"

### Notes

N/A

"""

def find_the_difference(s, t):
  for i in s:
    t = t.replace(i,'',1)
  return t

