"""


Write a function that finds the **longest word** in a sentence. If two or more
words are found, return the first longest word. Characters such as apostophe,
comma, period (and the like) count as part of the word (e.g. _O'Connor_ is 8
characters long).

### Examples

    longest_word("Margaret's toy is a pretty doll.") ➞ "Margaret's"
    
    longest_word("A thing of beauty is a joy forever.") ➞ "forever."
      
    longest_word("Forgetfulness is by all means powerless!") ➞ "Forgetfulness"

### Notes

A similar version of this challenge, which is to be implemented
**recursively** , can be found in
[here](https://edabit.com/challenge/LyzKTyYdKF4oDf5bG).

"""

def longest_word(s):
  s = s.split()
  x = ""
  for i in s:
    if len(i)>len(x):
      x=i
  return x

