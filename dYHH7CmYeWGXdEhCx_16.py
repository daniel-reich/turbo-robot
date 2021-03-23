"""


In this challenge, you have to build a word from the scrambled letters
contained in the first given list. For establishing how to assign the spots to
the letters, you will use the positions contained in the second given list.

    letters = ["e", "t", "s", "t"]
    positions = [1, 3, 2, 0]
    
    Step 1 ➞ Letter "e" goes to index 1 ➞ _  e  _   _
    Step 2 ➞ Letter "t" goes to index 3 ➞ _  e  _   t
    Step 3 ➞ Letter "s" goes to index 2 ➞ _  e  s   t
    Step 4 ➞ Letter "t" goes to index 0 ➞ t  e  s   t

Given the two lists `letters` (containing the scrambled letters of the word)
and `positions` (containing the indexes of the letters), implement a function
that returns the resulting word as a string.

### Examples

    wordBuilder(["e", "t", "s", "t"], [1, 3, 2, 0]) ➞ "test"
    
    wordBuilder(["b", "e", "t", "i", "d", "a"], [3, 0, 5, 4, 1, 2]) ➞ "edabit"
    
    wordBuilder(["g", "e", "o"], [1, 0, 2]) ➞ "ego"

### Notes

Every given test case has valid parameters, don't worry about exceptions
handling.

"""

def word_builder(l, p):
  return ''.join(i[0] for i in sorted(zip(l, p), key=lambda x: x[-1]))

