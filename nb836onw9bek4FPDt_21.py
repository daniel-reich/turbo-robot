"""


Given a sentence, return the number of words which have the **same first and
last letter**.

### Examples

    count_same_ends("Pop! goes the balloon") ➞ 1
    
    count_same_ends("And the crowd goes wild!") ➞ 0
    
    count_same_ends("No I am not in a gang.") ➞ 1

### Notes

  * Don't count single character words (such as "I" and "A" in example #3).
  * The function should not be case sensitive, meaning a capital "P" should match with a lowercase one.
  * Mind the punctuation!
  * Bonus points indeed for using regex!

"""

import re
​
def count_same_ends(txt):
  txt = re.sub(r'\W+', ' ', txt.lower())
  s = 0
  for i in txt.split(' '):
    if len(i) > 1 and i[0] == i[-1]:
      s += 1
  return s

