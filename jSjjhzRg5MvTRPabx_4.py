"""


Given a list of strings (nouns), list them up in a complete sentence.

### Examples

    sentence(["orange", "apple", "pear"]) ➞ "An orange, an apple and a pear."
    
    sentence(["keyboard", "mouse"]) ➞ "A keyboard and a mouse."
    
    sentence(["car", "plane", "truck", "boat"]) ➞ "A car, a plane, a truck and a boat."

### Notes

  * The sentence starts with a **capital letter**.
  * Do not change **the order** of the words.
  *  **A/An** should be correct in all places.
  * Put commas between nouns, except between the last two (there you put "and").
  * The sentence ends with a `.`
  * There are at least two nouns given.
  * Every given word is lowercase.

"""

def sentence(words):
  v='aeiou'
  A=[]
  for x in words:
    if x[0] in v:
      A.append('an')
    else:
      A.append('a')
  B=[x[0]+' '+x[1] for x in zip(A, words)]
  if len(words)==2:
    return ' and '.join(B).capitalize()+'.'
  else:
    return (', '.join(B[:-1])+' and '+B[-1]).capitalize()+'.'

