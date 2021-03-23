"""


Create a function that takes an array of strings of arbitrary dimensionality
(`[]`, `[][]`, `[][][]`, etc) and returns the deep_sum of every separate
number in each string in the array.

### Examples

    deep_sum(["1",  "five",  "2wenty",  "thr33"]) ➞ 36
    
    deep_sum([["1X2",  "t3n"], ["1024", "5", "64"]]) ➞ 1099
    
    deep_sum([[["1"], "10v3"],  ["738h"],  [["s0"],  ["1mu4ch3"], "-1s0"]]) ➞ 759

### Notes

  * Numbers in strings can be negative, but will all be base-10 integers.
  * Negative numbers may directly follow another number.
  * The hyphen or minus character ("-") does not only occur in numbers.
  * Arrays may be ragged or empty.

"""

def deep_sum(lst):
  def flatten_matrix(input_matrix):
    output = []
    for i in input_matrix:
      if type(i) != list:
        output.append(i)
      else:
        output += flatten_matrix(i)
    return output
  lst = flatten_matrix(lst)
  total = 0
  for i in lst:
    current_num = "0"
    for j in i:
      if j in "0123456789":
        current_num += j
      elif j == "-":
        total += int(current_num)
        current_num = "-0"
      else:
        total += int(current_num)
        current_num = "0"
    total += int(current_num)
  return total

