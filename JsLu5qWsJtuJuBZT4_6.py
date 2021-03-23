"""


Create a function that takes a string as the first argument, and a (string)
specification as a second argument. If the specification is `"word"`, return a
string with each word reversed while maintaining their original order. If the
specification is `"sentence",` reverse the order of the words in the string,
while keeping the words intact.

### Examples

    txt = "There's never enough time to do all the nothing you want"
    flip("Hello", "word") ➞ "olleH"
    
    flip("Hello", "sentence") ➞ "Hello"
    
    flip(txt, "word") ➞ "s'erehT reven hguone emit ot od lla eht gnihton uoy tnaw"
    
    flip(txt, "sentence") ➞ "want you nothing the all do to time enough never There's"

### Notes

N/A

"""

def flip(txt, spec):
  txt = txt.split(' ')
  if spec == 'word':
    return ' '.join(i[::-1] for i in txt)
  elif spec == 'sentence':
    return ' '.join(i for i in txt[::-1])

