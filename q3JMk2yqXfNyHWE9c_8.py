"""


Create a function that takes a word and returns `True` if the word has two
consecutive identical letters.

### Examples

    double_letters("loop") ➞ True
    
    double_letters("yummy") ➞ True
    
    double_letters("orange") ➞ False
    
    double_letters("munchkin") ➞ False

### Notes

N/A

"""

double_letters = lambda w: any(x*2 in w for x in w)

