"""


Given a string `worm` create a function that takes the length of the worm and
converts it into millimeters. Each `-` represents one centimeter.

### Examples

    worm_length("----------") ➞ "100 mm."
    
    worm_length("") ➞ "invalid"
    
    worm_length("---_-___---_") ➞ "invalid"

### Notes

Return `"invalid"` if an empty string is given or if the string has characters
other than `-`.

"""

def worm_length(hyphens):
    if hyphens == "":
        return "invalid"
    for character in hyphens:
        if character != "-":
            return "invalid"
    length = len(hyphens)
    return str(length * 10) + " mm."

