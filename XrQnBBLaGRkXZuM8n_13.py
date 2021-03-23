"""


Create a function that takes two inputs: `indexes` (a list of integers) and
`string` (a string). The function should return another string with the
letters of `string` at each index in `indexes` in order.

### Examples

    index_filter([2, 3, 8, 11], "Autumn in New York") ➞ "tune"
    
    index_filter([0, 1, 5, 7, 4, 2], "Cry me a river") ➞ "creamy"
    
    index_filter([9, -9, 2, 27, 36, 6, 5, 13, -1, 2, 0, 30, 2], 
      "That's life, I've got you under my skin") ➞ "frank sinatra"

### Notes

  * Indexes may not be in order / may be negative (see example #2 and #3).
  * The output string must always be lowercase, but the input `string` may not be (see examples).
  * Bonus points for submitting a `lambda` function.

"""

def index_filter(indexes, string):
  word = ''
  for i in indexes:
    word += string[i]
  return word.lower()

