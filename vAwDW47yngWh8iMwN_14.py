"""


Create a function that capitalizes the last letter of every word.

### Examples

    cap_last("hello") ➞ "hellO"
    
    cap_last("My Name Is Edabit") ➞ "MY NamE IS EdabiT"
    
    cap_last("HELp THe LASt LETTERs CAPITALISe") ➞ "HELP THE LAST LETTERS CAPITALISE"

### Notes

There won't be any cases of punctuation in the tests.

"""

def capLast(txt):
    txt = list(txt.split(' '))
    for i in range(len(txt)):
        txt[i] = txt[i][:-1]+txt[i][-1].upper()
    txt = ' '.join(txt)
    return txt

