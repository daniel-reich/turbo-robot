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
  out = ""
  split = txt.split(" ")
  for i in split:
    if len(i) >= 5:
      out += i[::-1] + " "
    else:
      out+= i + " "
  return out[:-1]

