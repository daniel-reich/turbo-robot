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

import itertools
​
def fit_words(words, clue):
    clue_no, clue_letter = clue    
    for perm in itertools.permutations(words):
        w1, w2, w3, w4, w5, w6, w7, w8, w9 = perm
        if perm[clue_no - 1][3] != clue_letter:
            continue
        if w1[0] == w5[-1] and w1[2] == w3[4] and w1[-1] == w4[-1] and \
           w2[0] == w3[0] and w2[4] == w4[2] and w2[-1] == w6[0] and \
           w3[2] == w5[4] and w3[-1] == w6[-1] and \
           w4[0] == w5[0] and w4[4] == w6[2]:
            return [w1, w2, w3, w4, w5, w6]

