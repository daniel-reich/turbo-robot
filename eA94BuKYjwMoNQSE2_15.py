"""


Create a function that returns `True` if a given inequality expression is
correct and `False` otherwise.

### Examples

    correct_signs("3 < 7 < 11") ➞ True
    
    correct_signs("13 > 44 > 33 > 1") ➞ False
    
    correct_signs("1 < 2 < 6 < 9 > 3") ➞ True

### Notes

N/A

"""

def correct_signs(txt):
    import re
    matches = re.finditer(r'(?=(\d{1,}\s\D\s\d{1,}))',txt)
    return all([eval(string) for string in [match.group(1) for match in matches]])

