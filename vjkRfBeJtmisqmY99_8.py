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

cross = [[], [(1, 4, 0, 4)], [(2, 4, 0, 2), (2, 6, 1, 6)], [(3, 4, 1, 2),
        (3, 6, 0, 6)], [(4, 0, 3, 0), (4, 4, 2, 2), (4, 6, 0, 0)],
        [(5, 0, 2, 0), (5, 2, 4, 2), (5, 4, 3, 2), (5, 6, 1, 0)]]
​
def fit_words(words, clue):
    def check(lst):
        return all(res[w1][i1]==res[w2][i2] for w1, i1, w2, i2 in lst)
    
    def fitnext(level):
        if level>5: return res[clue[0]-1][3] == clue[1]
        for i, word in enumerate(words):
            if used[i]: continue
            res[level] = word
            used[i] = True
            if check(cross[level]) and fitnext(level+1):
                return True
            used[i] = False
            
    used = [False] * 9
    res = [None] * 6
    fitnext(0)
    res[1], res[5] = res[5], res[1]
    return res

