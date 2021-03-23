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
    c = ' '
    txt = txt + c
    master = [pos for pos, char in enumerate(txt) if char == c]
    if length in master:
        return txt[0:length]
    else:
        new_list = sorted(master + [length])
        offst = new_list.index(length)
        if offst == 0:
            return ""
        else:
            offst -= 1
            new_index = new_list[offst]
            return txt[0:new_index]

