"""


You are given two inputs:

  1. An array of abbreviations.
  2. An array of words.

Write a function that returns `True` if each abbreviation **uniquely
identifies** a word, and `False` otherwise.

### Examples

    unique_abbrev(["ho", "h", "ha"], ["house", "hope", "happy"]) ➞ False
    // "ho" and "h" are ambiguous and can identify either "house" or "hope"
    
    unique_abbrev(["s", "t", "v"], ["stamina", "television", "vindaloo"]) ➞ True
    
    unique_abbrev(["bi", "ba", "bat"], ["big", "bard", "battery"]) ➞ False
    
    unique_abbrev(["mo", "ma", "me"], ["moment", "many", "mean"]) ➞ True

### Notes

Abbreviations will be a substring from `[0, n]` from the original string.

"""

def unique_abbrev(abbs, words):
    a=[]
    if abbs[0]==words[1][:2] or abbs[0]==words[1][:2]:
        a.append('f')
    elif abbs[1]==words[0][:2] or abbs[1]==words[2][:2]:
        a.append('f')
    elif abbs[2]==words[0][:2] or abbs[2]==words[1][:2]:
        a.append('f')
    else:
        a.append('t')
    if 'f' in a:
        return False
    else:
        return True

