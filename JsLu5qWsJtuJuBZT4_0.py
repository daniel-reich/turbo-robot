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
  print(txt)
  if spec == "word":
    if ' ' not in txt:
      return txt[::-1]    
    return ' '.join([word[::-1] for word in txt.split(' ')])
  elif spec == "sentence":
    return ' '.join([word for word in txt.split(' ')[::-1]])

