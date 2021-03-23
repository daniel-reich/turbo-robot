"""


Create a function that flips M's to W's (all uppercase).

### Examples

    wumbo("I LOVE MAKING CHALLENGES") ➞ "I LOVE WAKING CHALLENGES"
    
    wumbo("MEET ME IN WARSAW") ➞ "WEET WE IN WARSAW"
    
    wumbo("WUMBOLOGY") ➞ "WUWBOLOGY"

### Notes

N/A

"""

def wumbo(words):
    wumbo_sentence = []
    for letter in words:
        if letter == 'M':
            wumbo_sentence.append('W')
        else:
            wumbo_sentence.append(letter)
    return ''.join(wumbo_sentence)

