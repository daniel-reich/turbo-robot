"""


Create a function that returns `True` if an input string contains only
uppercase or only lowercase letters.

### Examples

    same_case("hello") ➞ True
    
    same_case("HELLO") ➞ True
    
    same_case("Hello") ➞ False
    
    same_case("ketcHUp") ➞ False

### Notes

N/A

"""

same_case = lambda txt : txt.isupper() or txt.islower()

