"""


Create a function that takes a string, removes all "special" characters (e.g.
`., !, @, #, $, %, ^, &, \, *, (, )`) and returns the new string. The only
non-alphanumeric characters allowed are dashes `-`, underscores `_` and
spaces.

### Examples

    remove_special_characters("The quick brown fox!") ➞ "The quick brown fox"
    
    remove_special_characters("%fd76$fd(-)6GvKlO.") ➞ "fd76fd-6GvKlO"
    
    remove_special_characters("D0n$c sed 0di0 du1") ➞ "D0nc sed 0di0 du1"

### Notes

N/A

"""

def remove_special_characters(txt):
    l = []
    for item in txt:
        if item in ['-','_',' '] or 'A'<=item<= 'Z'or 'a'<=item<='z' or '0'<=item<='9'  :
            l.extend(item)
    print(l)
    return ''.join([item for item in l])

