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
    voels = ['a','e','i','o','u']
    newtxt=''
    for i in range(len(txt)):
        if txt[i] in voels:
            newtxt+=ch
        else:
            newtxt += txt[i]
    return newtxt

