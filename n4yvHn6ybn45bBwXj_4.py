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

x = "[0-9]*[02468]$" # write the regular expression

