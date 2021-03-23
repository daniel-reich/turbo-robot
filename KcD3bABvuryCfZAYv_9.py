"""


Write a function that returns the most frequent character in a list of words.

### Examples

    most_frequent_char(["apple", "bandage", "yodel", "make"])
    ➞ ["a", "e"]
    
    most_frequent_char(["music", "madness", "maniac", "motion"])
    ➞ ["m"]
    
    most_frequent_char(["the", "hills", "are", "alive", "with", "the", "sound", "of", "music"])
    ➞ ["e", "h", "i"]

### Notes

  * If multiple characters tie for most frequent, list all of them in alphabetical order.
  * Words will be in lower case.

"""

def most_frequent_char(lst):
    stringy = ""
    diccy  ={}
    seccy = {}
    for i in lst:
        for j in i:
            stringy = stringy + j
    setty = set(stringy)
    for p in setty:
        diccy[p] = stringy.count(p)
    revvy = {}
    for key, value in diccy.items():
        revvy[value] = revvy.get(value, []) + [key]
    #print(revvy)
    maxy = max(revvy)
    return sorted((revvy[maxy]))

