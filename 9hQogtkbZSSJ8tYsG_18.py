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
  return "".join([txt[letter].upper() if txt[letter].islower() else txt[letter].lower() for letter in range(len(txt)-1,-1,-1) ])

