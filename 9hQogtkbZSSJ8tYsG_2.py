"""


The "Reverser" takes a string as input and returns that string in reverse
order, with the opposite case.

### Examples

    reverse("Hello World") ➞ "DLROw OLLEh"
    
    reverse("ReVeRsE") ➞ "eSrEvEr"
    
    reverse("Radar") ➞ "RADAr"

### Notes

There will be no punctuation in any of the test cases.

"""

def reverse(txt):
  return ''.join([i.lower() if i==i.upper() else i.upper() for i in txt])[::-1]

