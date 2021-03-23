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
    dicionario, pl, parou, atual, posicao =dict(), [''], [0], 0, 0
    total, maximo = len(string), max([len(i) for i in lst])
    for i in lst: dicionario[i] = True
    while len(pl):
        for letra in range(min(maximo,total-posicao)):
            pl[atual] += string[posicao]; posicao += 1
            if pl[atual] in dicionario:
                if posicao == total: return ' '.join(pl)
                else: parou.append(posicao); pl.append(''); atual += 1; break
        if pl[atual] != '':
            pl.pop(); posicao = parou[atual]; atual -= 1; parou.pop()
    return "Cleaving stalled: Word not found"

