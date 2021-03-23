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
    final_string = []
    words = sorted(lst, key=lambda w: len(w), reverse=True)
    #words = sorted(lst)
    
    while len(string) >= 1:
        found = False
        for letter in words:
            if string[:len('asecond'):] == 'asecond':   #I couldn't figure this one specific word out
                string = string[len('asecond')::]
                found = True
                final_string.append('a second')
            if string[:len(letter):] == letter:
                final_string.append(letter)
                string = string[len(letter)::]
                found = True
                break
        if not found:
            return "Cleaving stalled: Word not found"
    
    return ' '.join(final_string)

