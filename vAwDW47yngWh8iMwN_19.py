"""


Create a function that capitalizes the last letter of every word.

### Examples

    cap_last("hello") ➞ "hellO"
    
    cap_last("My Name Is Edabit") ➞ "MY NamE IS EdabiT"
    
    cap_last("HELp THe LASt LETTERs CAPITALISe") ➞ "HELP THE LAST LETTERS CAPITALISE"

### Notes

There won't be any cases of punctuation in the tests.

"""

def capitlise_end(w):
  return w[:-1] + chr(ord(w[-1])-32) if 'a' <= w[-1] <= 'z' else w
​
def cap_last(txt):
  return ' '.join(capitlise_end(w) for w in txt.split(' '))

