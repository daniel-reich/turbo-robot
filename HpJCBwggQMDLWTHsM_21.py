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
  if(txt == ""):
    return 0
  else:
    lst = list(txt.strip().split(' '))
    t = 0
    s = 0
    for elem in lst:
      kk = list(elem.strip())
      t += len(kk)
      if(kk[-1].isalpha()):
        t = t
      else:
        t -= 1
      s += 1
    T = float(t)
    S = float(s)
    p = float(float(T)/float(S))
    P = round(p,2)
    return P

