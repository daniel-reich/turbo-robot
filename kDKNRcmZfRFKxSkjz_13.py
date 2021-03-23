"""


 _lPaeesh le pemu mnxit ehess rtnisg!_ Oh, sorry, that was supposed to say:
_Please help me unmix these strings!_

Somehow my strings have all become mixed up; every pair of characters has been
swapped. Help me undo this so I can understand my strings again.

### Examples

    unmix("123456") ➞ "214365"
    
    unmix("hTsii  s aimex dpus rtni.g") ➞ "This is a mixed up string."
    
    unmix("badce") ➞ "abcde"

### Notes

The length of a string can be odd — in this case the last character is not
altered (as there's nothing to swap it with).

"""

def unmix(txt):
    new_string = ""
    if len(txt) % 2 == 0:
        for i in range(0, len(txt), 2):
            new_string = new_string + txt[i+1]
            new_string = new_string + txt[i]
    else:
        for i in range(0, len(txt)-1, 2):
            new_string = new_string + txt[i+1]
            new_string = new_string + txt[i]
        new_string = new_string + txt[len(txt) - 1]
    return new_string
