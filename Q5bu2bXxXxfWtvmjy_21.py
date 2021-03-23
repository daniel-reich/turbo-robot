"""


Given a string of letters in the English alphabet, return the letter that's
missing from the string. The missing letter will make the string be in
alphabetical order (from A to Z).

If there are no missing letters in the string, return `"No Missing Letter"`.

### Examples

    missing_letter("abdefg") ➞ "c"
    
    missing_letter("mnopqs") ➞ "r"
    
    missing_letter("tuvxyz") ➞ "w"
    
    missing_letter("ghijklmno") ➞ "No Missing Letter"

### Notes

The given string will never have more than one missing letter.

"""

from string import ascii_lowercase
​
​
def missing_letter(txt):
    lowest_index = ascii_lowercase.index(txt[0])
    highest_index = ascii_lowercase.index(txt[-1])
    for ch in ascii_lowercase[lowest_index:highest_index + 1]:
        if ch not in txt:
            return ch
    return 'No Missing Letter'

