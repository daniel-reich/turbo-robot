"""


Given a _list of words_ , return the **longest word** which can fit on a _7
segment display_.

![Image of a 7 segment display](https://edabit-
challenges.s3.amazonaws.com/clock_xkmdxe.jpeg)

  * Letters which do not fit on a _7 segment display_ are **k** , **m** , **v** , **w** and **x**.
  * Therefore, do not count words which include these letters.

### Examples

    longest_7segment_word(["knighthood", "parental", "fridge", "clingfilm"]) ➞ "parental"
    
    longest_7segment_word(["coding", "crackers", "edabit", "celebration"]) ➞ "celebration"
    
    longest_7segment_word(["velocity", "mackerel", "woven", "kingsmen"]) ➞ ""

### Notes

  * All words will be given in lowercase.
  * Return an _empty string_ if no words are eligible (see example #3).
  * If multiple valid words have the same length, return the **first word that appears**.

"""

def longest_7segment_word(lst):
  qualifies = []
  for word in lst:
    nogood = False
    for letter in word:
      if letter in ['k', 'v', 'm', 'w', 'x']:
        nogood = True
    if nogood:
      continue
    qualifies.append(word)
  if qualifies:
    temp = list(map(len, qualifies))
    return qualifies[temp.index(max(temp))]
  else:
    return ""

