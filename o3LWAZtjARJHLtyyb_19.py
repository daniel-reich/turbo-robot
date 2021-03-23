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
  x = ""
  for char in txt:
    if char.islower() :
      x= x+char.upper()
    else:
      x =x+char.lower()
  return x

