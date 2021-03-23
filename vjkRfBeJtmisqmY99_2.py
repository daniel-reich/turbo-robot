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
 
POINTS3 = (2, (0,1,0), (2,4,4), (4,0,2), (6,5,6))
# intersections of word 3 with others in (word 3 letter intersection index,
# other word number (from 0), other word intersection letter index) format
​
POINTS4 = (3, (0,4,0), (2,1,4), (4,5,2), (6,0,6))
# intersections of word 4 with others in (word 4 letter intersection index,
# other word number (from 0), other word intersection letter index) format
​
POINTS1 =(0, (0,4,6))
POINTS2 = (1, (6,5,0))
# intersections of words 1 & 2 with others in (word 1/2 letter intersection index,
# other word number (from 0), other word intersection letter index) format
​
CROSSES = (POINTS3,POINTS4,POINTS1,POINTS2)  # to be used to check above crossing points
​
def words_mesh(words):
    '''
    Returns True if the words supplied mesh according to the star intersection
    rules, otherwise False
    '''
    for cross_set in CROSSES:
        check_word_pos = cross_set[0]
        for i in range(1, len(cross_set)):
            check_letter_pos, word_pos, letter_pos = cross_set[i]
            if words[check_word_pos][check_letter_pos] != words[word_pos][letter_pos]:
                return False  # not this set of words in this order
            
    return True  # passed all the tests
​
​
def fit_words(words, clue):
    '''
    Generates the words to be checked for correct intersections.
    Returns the words in order when found
    '''
    clue_word_pos = clue[0] - 1  # where the clue word fits in the star
    answers = []
    
    for clue_word in [word for word in words if word[3] == clue[1]] :
        word_set = list(set(words) - set([clue_word])) # target words to check
        
        
        for words2 in permutations(word_set, 5): # Get each set of 5 words
            # Insert the clue word in its correct position
            words2 = words2[:clue_word_pos] + (clue_word,) + words2[clue_word_pos:]
            if words_mesh(words2):
                answers.append(list(words2))   # words found
​
    return None if not answers else answers[0] # may be > 1

