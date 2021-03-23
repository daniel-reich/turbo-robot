"""


Create a function that takes a string (without spaces) and a word list,
cleaves the string into words based on the list, and returns the correctly
spaced version of the string (a sentence). If a section of the string is
encountered that can't be found on the word list, return `"Cleaving stalled:
Word not found"`.

### Examples

    word_list = ["about", "be", "hell", "if", "is", "it", "me", "other", "outer", "people", "the", "to", "up", "where"]
    cleave("ifitistobeitisuptome", word_list) ➞ "if it is to be it is up to me"
    
    cleave("hellisotherpeople", word_list) ➞ "hell is other people"
    
    cleave("hellisotterpeople", word_list) ➞ "Cleaving stalled: Word not found"

### Notes

Words on the `word_list` can appear more than once in the string. The
`word_list` is a reference guide, kind of like a dictionary that lists which
words are allowed.

"""

def cleave(string, lst):
    def words(word, string, i):
        while True:
            if string[0:i] in lst:
                word.append(string[0:i])
                string = string[i::]
                i = 0 
                if string == '':
                    break
            elif i == len(string):
                a = word.pop()
                words(word, a + string, len(a) + 1)
            elif i > len(string):
                break
            i += 1
    word = []
    try:
        words(word, string, 1)
    except:
        word = ['Cleaving stalled: Word not found']
    return ' '.join(word)

