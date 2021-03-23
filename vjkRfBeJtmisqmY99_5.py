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

from itertools import permutations
def fit_words(w, clue):
    w_pos, char = clue
    for w_idx, word in enumerate(w):
        if word[3] == char:
            rem_idx = [i for i in range(9) if i != w_idx]
            for tpl_p in permutations(rem_idx, 5):
                p = list(tpl_p)
                p = p[: w_pos - 1] + [w_idx] + p[w_pos - 1:]
                if (w[p[0]][0] == w[p[4]][6] and w[p[0]][2] == w[p[2]][4] and
                    w[p[0]][6] == w[p[3]][6] and w[p[1]][0] == w[p[2]][0] and
                    w[p[1]][4] == w[p[3]][2] and w[p[1]][6] == w[p[5]][0] and
                    w[p[2]][2] == w[p[4]][4] and w[p[2]][6] == w[p[5]][6] and
                    w[p[3]][0] == w[p[4]][0] and w[p[3]][4] == w[p[5]][2]):
                    return [w[w_idx] for w_idx in p]
    return -1

