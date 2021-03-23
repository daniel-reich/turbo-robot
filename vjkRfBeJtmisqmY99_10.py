"""


You are given a list of 9 7-letter words. You are also given the middle letter
of one of the 6 of them which fit together in a sort of star pattern as
follows:

Word 1 fits diagonally downwards from left to right. Its 1st letter is the
last letter of word 5; 3rd letter the 5th of word 3;last letter the last
letter of word 4.

Word 2 fits diagonally downwards from left to right. Its 1st letter is the 1st
letter of word 3; 5th letter the 3rd of word 4; last letter the 1st of word 6.

Word 3 fits horizontally from left to right. Its 1st letter is the 1st of word
2; 3rd the 5th of word 5; 5th the 3rd of word 1; last the last of word 6.

Word 4 fits horizontally from left to right. Its 1st letter is the 1st of word
5; 3rd the 5th of word 2; 5th the 3rd of word 6; last the last of word 1.

Word 5 fits diagonally upwards from left to right. Its 1st letter is the 1st
letter of word 4; 5th the 3rd letter of word 3; last the 1st of word 1.

Word 6 fits diagonally upwards from left to right. Its 1st letter is the last
of word 2; 3rd the 5th of word 4; last the last of word 3.

Write a function which takes in a list of 9 7-letter words and number of one
of the words and its middle letter and outputs a list of the 6 words which fit
together as above, ordered as words 1 to 6 as described. For some tests there
may be more than 1 correct answer - any will be accepted.

 **Examples**

fit_words(["crudity", 'reactor', 'grammar', 'bromide', 'aridity', 'airport',
'trilogy', 'rhizome', 'barrier' ](),(3,'d')) --> ['rhizome', 'airport',
'aridity', 'bromide', 'barrier', 'trilogy']()

fit_words(['station', 'freezer', 'sulfate', 'portion', 'trilogy', 'typhoon',
'solvent', 'episode', 'steeple' ](),(3,'e')) --> ['typhoon', 'sulfate',
'steeple', 'station', 'solvent', 'episode']()

 **Notes**

Words are numbered from 1 (so the clue word in each of the examples is the 3rd
word)

Case may be ignored - all test words are lower case.

"""

def word3(w1,w2,w3):
  if w3 == w1 or w3 == w2:
    return False
  return w2[0]==w3[0] and w3[4] == w1[2]
def word4(w1,w2,w3,w4):
  if w4 == w1 or w4 == w2 or w4 == w3:
    return False
  return w4[2] == w2[4] and w1[6] == w4[6]
def word5(w1,w2,w3,w4,w5):
  if w1 == w5 or w2 == w5 or w3 == w5 or w4 == w5:
    return False
  return w4[0] == w5[0] and w5[4] == w3[2] and w5[6] == w1[0]
def word6(w1,w2,w3,w4,w5,w6):
  if w1 == w6 or w2 == w6 or w3 == w6 or w4 == w6 or w5 == w6:
    return False
  return w6[0] == w2[6] and w6[2] == w4[4] and w6[6] == w3[6] 
def fit_words(words, clue):
  path = []
  for w1 in words:
    for w2 in list(filter(lambda x: x != w1,words)):
      for w3 in list(filter(lambda x: x[3] == clue[1] and word3(w1,w2,x),words)):
        for w4 in list(filter(lambda x: word4(w1,w2,w3,x),words)):
          for w5 in list(filter(lambda x: word5(w1,w2,w3,w4,x),words)):
            for w6 in list(filter(lambda x: word6(w1,w2,w3,w4,w5,x),words)):
              path.append([w1,w2,w3,w4,w5,w6])
  return path[0]

