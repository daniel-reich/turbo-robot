"""


Create a function that takes a string and returns the letters that **occur
only once**.

### Examples

    find_letters("monopoly") ➞ ["m", "n", "p", "l", "y"]
    
    find_letters("balloon") ➞ ["b", "a", "n"]
    
    find_letters("analysis") ➞ ["n", "l", "y", "i"]

### Notes

  * The final list should not include letters that appear more than once in the string.
  * Return the letters in the sequence they were originally in, do not sort them.
  * All letters will be in lowercase.

"""

def find_letters(word):
  lst = [l for l in word if word.count(l) <= 1]
  return lst

