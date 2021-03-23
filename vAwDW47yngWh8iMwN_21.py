"""


Create a function that capitalizes the last letter of every word.

### Examples

    cap_last("hello") ➞ "hellO"
    
    cap_last("My Name Is Edabit") ➞ "MY NamE IS EdabiT"
    
    cap_last("HELp THe LASt LETTERs CAPITALISe") ➞ "HELP THE LAST LETTERS CAPITALISE"

### Notes

There won't be any cases of punctuation in the tests.

"""

def cap_last(s):
    lst = s.split(" ")
    newLst = []
    for w in lst:
        newLst.append(w[:len(w)-1] + w[len(w)-1].capitalize());
    return " ".join(newLst)

