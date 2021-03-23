"""


Write a regular expression that matches only an **even number**. Numbers will
be presented as strings.

### Examples

    "2341" ➞ false
    
    "132" ➞ true
    
    "29" ➞ false
    
    "5578" ➞ true

### Notes

This challenge is designed for **RegEx only**.

"""

x = "^\d*?((0)|(2)|(4)|(6)|(8))$" # write the regular expression

