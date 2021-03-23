"""


Create a function that takes a list of words and transforms it into a list of
each word's length.

### Examples

    word_lengths(["hello", "world"]) ➞ [5, 5]
    
    word_lengths(["Halloween", "Thanksgiving", "Christmas"]) ➞ [9, 12, 9]
    
    word_lengths(["She", "sells", "seashells", "down", "by", "the", "seashore"]) ➞ [3, 5, 9, 4, 2, 3, 8]

### Notes

  * No test case will contain punctuation.
  * Lists can be of various lengths.

"""

word_lengths=lambda l:list(map(len,l))

