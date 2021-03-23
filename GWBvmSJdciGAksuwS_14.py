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
  list = []
  counter = 0
  for i in word:
    counter = word.count(i)
    if counter == 1:
      list.append(i)
  return list

