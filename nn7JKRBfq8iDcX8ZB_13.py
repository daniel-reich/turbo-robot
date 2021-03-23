"""


Write a function that returns a **lambda expression** , which transforms its
input by adding a particular `suffix` at the end.

### Examples

    add_ly = add_suffix("ly")
    
    add_ly("hopeless") ➞ "hopelessly"
    add_ly("total") ➞ "totally"
    
    add_less = add_suffix("less")
    
    add_less("fear") ➞ "fearless"
    add_less("ruth") ➞ "ruthless"

### Notes

N/A

"""

def add_suffix(suffix):
    return lambda x:  x + suffix

