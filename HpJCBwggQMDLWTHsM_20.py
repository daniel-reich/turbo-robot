"""


Create a function that takes in a sentence and returns the average length of
each word in that sentence. Round your result to two decimal places.

### Examples

    average_word_length("A B C.") ➞ 1.00
    
    average_word_length("What a gorgeous day.") ➞ 4.00
    
    average_word_length("Dude, this is so awesome!") ➞ 3.80

### Notes

Ignore punctuation when counting the length of a word.

"""

import string as s
​
def average_word_length(txt):
  cln = txt.translate(str.maketrans('', '', s.punctuation)).split()
  return round(sum(len(x) for x in cln)/len(cln),2)

