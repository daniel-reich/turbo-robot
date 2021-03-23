"""


Create a function to calculate how many characters in total are needed to make
up the shape. You will be given a list of strings which make up a shape in the
compiler (i.e. a square, a rectangle or a line).

### Examples

    count_characters([
      "###",
      "###",
      "###"
    ]) ➞ 9
    
    count_characters([
      "22222222",
      "22222222",
    ]) ➞ 16
    
    count_characters([
      "------------------"
    ]) ➞ 18
    
    count_characters([]) ➞ 0
    
    count_characters(["", ""]) ➞ 0

### Notes

Return `0` if the given list is empty.

"""

def count_characters(lst):
  return sum([len(i) for i in lst])

