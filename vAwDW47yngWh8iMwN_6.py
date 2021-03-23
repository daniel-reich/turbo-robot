"""


Create a function that capitalizes the last letter of every word.

### Examples

    cap_last("hello") ➞ "hellO"
    
    cap_last("My Name Is Edabit") ➞ "MY NamE IS EdabiT"
    
    cap_last("HELp THe LASt LETTERs CAPITALISe") ➞ "HELP THE LAST LETTERS CAPITALISE"

### Notes

There won't be any cases of punctuation in the tests.

"""

def cap_last(st):
    l2 = []
    for a in st.split():
        l1 = []
        for b in a:
            l1.append(b)
        l1[-1] = l1[-1].upper()
        l2.append(''.join(l1))
    return ' '.join(l2)

