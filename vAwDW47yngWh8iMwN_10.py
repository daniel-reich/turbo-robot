"""


Create a function that capitalizes the last letter of every word.

### Examples

    cap_last("hello") ➞ "hellO"
    
    cap_last("My Name Is Edabit") ➞ "MY NamE IS EdabiT"
    
    cap_last("HELp THe LASt LETTERs CAPITALISe") ➞ "HELP THE LAST LETTERS CAPITALISE"

### Notes

There won't be any cases of punctuation in the tests.

"""

def cap_last(txt):
  lst = txt.split(" ")
  newstr = ""
  for x in lst:
    y = len(x)
    newstr = newstr + " " + x[:y - 1] + x[y - 1].upper()
  newstr = newstr.strip()
​
  return newstr

