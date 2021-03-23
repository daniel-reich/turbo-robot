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

intersects =[
   [(4,6), (2,4), (5,4), (3,6)],
     [(2,0), (4,2), (3,2), (5,1)],
     [(1,0), (4,4), (0,2), (5,6)],
     [(4,0), (1,4), (5,2), (0,6)],
     [(3,0), (1,2), (2,2), (0,0)],
     [(1,6), (3,4), (0,4), (2,6)]]
​
fit_order = [2,1,5,0,3,4]
​
def fit_next_word(sln, fit_order_index, words):
    fit_order_index = (fit_order_index+1)%6
    isect_list_index = fit_order[fit_order_index]
    for cw in words:
        is_poss = True
        for i, s in enumerate(intersects[isect_list_index]):
            soln_index, isect = s
            if sln[soln_index] and sln[soln_index][isect] != cw[i*2]:
                is_poss = False
                break
        if is_poss:
            sln[isect_list_index] = cw
            fit_next_word(sln, fit_order_index, list(filter(lambda w: w != cw, words)))
            if all(w for w in sln): return
            sln[isect_list_index] = ''
    return 
​
def fit_words(words, clue):
    wix = clue[0]-1
    cix = fit_order.index(wix)
    for cw in filter(lambda w: w[3] == clue[1], words):
        sln = ['']*6
        sln[wix] = cw
        fit_next_word(sln, cix, list(filter(lambda w: w != cw, words)))
        if all(w for w in sln): return sln
    return None

