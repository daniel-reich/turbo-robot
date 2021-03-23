"""


Create a function that replaces all the vowels in a string with a specified
character.

### Examples

    replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"
    
    replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"
    
    replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"

### Notes

All characters will be in lower case.

"""

def replace_vowels(txt, ch):
    list1 = list(txt)
    for i in range(len(list1)):
        if list1[i] in ["a","e","i","o","u"]:
            list1[i] = ch
    return "".join(list1)

