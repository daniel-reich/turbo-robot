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
  return ''.join([letter.upper() if letter.islower() else letter.lower() for letter in txt])

