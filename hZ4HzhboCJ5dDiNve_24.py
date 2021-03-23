"""


Create a function that takes a string and returns the reversed string. However
there's a few rules to follow in order to make the challenge interesting:

  * The UPPERCASE/lowercase positions must be kept in the same order as the original string (see example #1 and #2).
  * Spaces must be kept in the same order as the original string (see example #3).

### Examples

    special_reverse_string("Edabit") ➞ "Tibade"
    
    special_reverse_string("UPPER lower") ➞ "REWOL reppu"
    
    special_reverse_string("1 23 456") ➞ "6 54 321"

### Notes

N/A

"""

def special_reverse_string(txt):
    up = []
    space = []
    for i in range(len(txt)):
        if txt[i].isupper():
            up.append(i)
        elif txt[i] == ' ':
            space.append(i)
    reverse = list(txt.replace(' ','').lower()[::-1])
    for i in space:
        reverse.insert(i," ")
    for i in up:
        reverse[i] = reverse[i].upper()
    return ''.join(reverse)

