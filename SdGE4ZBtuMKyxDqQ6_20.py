"""


Create a function that takes a string and returns the first character that
repeats. If there is no repeat of a character, then return "-1".

### Examples

    first_repeat("legolas") ➞ "l"
    
    first_repeat("Gandalf") ➞ "a"
    
    first_repeat("Balrog") ➞ "-1"
    
    first_repeat("Isildur") ➞ "-1"

### Notes

Tests are case sensitive.

"""

def first_repeat(chars):
    hist = {}
    for char in chars:
        if char not in hist:
            hist[char] = 1
        else:
            hist[char] += 1
        
    for k,v in hist.items():
        if v > 1:
            return k  
    return str(-1)

