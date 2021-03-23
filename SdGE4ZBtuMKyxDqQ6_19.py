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
    for i in range(len(chars)):
        for j in range(len(chars)):
            if chars[i] == chars[j] and i != j:
                print(chars[j])
                return chars[j]
    return "-1"

