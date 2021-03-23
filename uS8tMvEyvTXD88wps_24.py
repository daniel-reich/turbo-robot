"""


Write a function that takes a string of one or more words as an argument and
returns the same string, but with all five or more letter words reversed.
Strings passed in will consist of only letters and spaces. Spaces will be
included only when more than one word is present.

### Examples

    reverse("Reverse") ➞ "esreveR"
    
    reverse("This is a typical sentence.") ➞ "This is a lacipyt .ecnetnes"
    
    reverse("The dog is big.") ➞ "The dog is big."

### Notes

You can expect a valid string to be provided for each test case.

"""

def reverse(txt):
  
  if " " in txt:
    txt = txt.split()
  else:
    if len(txt) >= 5:
      return txt[::-1]
    else:
      return txt
  
  result = ""
  for word in txt:
    if len(word) >= 5:
      result += word[::-1] + " "
    else:
      result += word + " "
  
  return result[:-1]

