"""


Creates a function that takes a string and returns the concatenated first and
last character.

### Examples

    first_last("ganesh") ➞ "gh"
    
    first_last("kali") ➞ "ki"
    
    first_last("shiva") ➞ "sa"
    
    first_last("vishnu") ➞ "vu"
    
    first_last("durga") ➞ "da"

### Notes

There is no empty string.

"""

first_last=lambda n:n[0]+n[-1]

