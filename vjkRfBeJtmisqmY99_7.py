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

def fit_words(words, clue):
    sols3 = [[w] for w in words if w[3] == clue[1]]
    sols13 = [[w]+s for w in words for s in sols3
              if w[2] == s[0][4] and w not in s]
    sols123 = [[s[0], w, s[1]] for w in words for s in sols13
               if w[0] == s[1][0] and w not in s]
    sols1234 = [s + [w] for w in words for s in sols123
                if w[-1] == s[0][-1] and w[2] == s[1][4] and w not in s]
    sols12345 = [s + [w] for w in words for s in sols1234
                 if w[0] == s[3][0] and w[2] == s[1][2] and
                 w[4] == s[2][2] and w not in s]
    sols = [s + [w] for w in words for s in sols12345
            if w[0] == s[1][-1] and w[2] == s[3][4] and
            w[4] == s[0][4] and w[-1] == s[2][-1] and w not in s]
​
    return sols[0]

