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
    if " " not in txt[0:length]:
        return ""
    if length > len(txt):
        return txt
    if txt[length] == " ":
        return txt[0:length]
    marker = 0
    for i in range(length):
        if txt[i] == " ":
            marker = i
    return txt[0:marker]

