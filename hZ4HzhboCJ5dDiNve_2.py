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
    new_txt = []
    special_reversed = []
    for char in reversed(txt):
        if char != " ":
            new_txt.append(char.lower())
​
    j = 0
    for i in range(0, len(txt)):
​
        if txt[i] != " " and txt[i].isupper():
            special_reversed.append(new_txt[j].upper())
            j += 1
        elif txt[i] == " ":
            special_reversed.append(" ")
        else:
            special_reversed.append(new_txt[j])
            j += 1
​
    return "".join(special_reversed)

