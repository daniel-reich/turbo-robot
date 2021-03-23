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
  lst = txt.split(" ")
  lst2 = []
  for i in range(0, len(lst)):
    if len(lst[i]) > 4 and i != len(lst)-1:
      lst2.append(lst[i][::-1] + " ")
    elif len(lst[i]) > 4 and i == len(lst)-1:
      lst2.append(lst[i][::-1])
    elif i == len(lst)-1:
      lst2.append(lst[i])
    else:
      lst2.append(lst[i] + " ")
  return "".join(lst2)

