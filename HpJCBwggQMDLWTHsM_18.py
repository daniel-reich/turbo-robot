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

def average_word_length(txt):
  arr = []
  txt = txt.replace(",","")
  txt = txt.replace(".","")
  txt = txt.replace("?","")
  txt = txt.replace("!","")
  for w in txt.split():
    arr.append(len(w))
  return round(sum(arr) / len(arr),2)

