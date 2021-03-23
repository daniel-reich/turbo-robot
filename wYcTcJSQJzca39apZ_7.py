"""


Create a function that takes a string (the string to truncate) and a number
(the _maximum_ length of the truncated string) as arguments and returns the
truncated string at the given length.

### Examples

    truncate("Lorem ipsum dolor sit amet.", 11) ➞ "Lorem ipsum"
    
    truncate("Lorem ipsum dolor sit amet.", 16) ➞ "Lorem ipsum"
    
    truncate("Lorem ipsum dolor sit amet.", 17) ➞ "Lorem ipsum dolor"

### Notes

  * To "truncate" means _"to shorten by cutting off the top or end"_.
  * If a word is truncated in the middle, discard it in the output (see 2nd example above).

"""

def truncate(txt, length):
    strn = ''
    c = 0
    for i in range(length):
        try:
            strn += txt[c]
            c += 1
        except IndexError:
            return txt
    if txt[c].isalpha():
        for l in strn[::-1]:
            if l == ' ':
                strn = strn[:-1]
                break
            elif l.isalpha():
                strn = strn[:-1]
    return strn

