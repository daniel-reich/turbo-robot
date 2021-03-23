"""


Given a string, create a function to reverse the case. All lower-cased letters
should be upper-cased, and vice versa.

### Examples

    reverse_case("Happy Birthday") ➞ "hAPPY bIRTHDAY"
    
    reverse_case("MANY THANKS") ➞ "many thanks"
    
    reverse_case("sPoNtAnEoUs") ➞ "SpOnTaNeOuS"

### Notes

N/A

"""

def reverse_case(txt):
  revtxt = ''
  for i in range(len(txt)):
    if txt[i].isupper():
      revtxt += txt[i].lower()
    else:
      revtxt += txt[i].upper()
  return revtxt

