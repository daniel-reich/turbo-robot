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

import string
​
def reverse_case(txt):
​
    upper_letters = string.ascii_uppercase
​
    transformed_letters = [char.lower() if char in upper_letters
                           else char.upper()
                           for char in txt]
​
    return ''.join(transformed_letters)

