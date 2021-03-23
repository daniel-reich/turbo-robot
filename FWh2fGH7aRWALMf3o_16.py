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

def cleave(string,lst):
    phrase = cleaveHelper(string,lst,[])
    if phrase:
        return ' '.join(phrase)
    else:
        return "Cleaving stalled: Word not found"
​
def cleaveHelper(string,words,lst):
    if len(string) == 0:
        return lst
    if len([i for i in words if i in string]) == 0:
        return None
    else:
        letter = string[0]
        options = []
        for word in words:
            l = len(word)
            if string[:l] == word:
                options.append(word)
        if len(options) == 1:
            l = len(options[0])
            lst.append(options[0])
            string = string[l:]
            return cleaveHelper(string,words,lst)
        else:
            for option in options:
                l = len(option)
                result = cleaveHelper(string[l:],words,lst+[option])
                if result:
                    return result

