"""


Given a string including a bunch of _characters and numbers_ , return the
**sum** of all the numbers in the string. Note that multiple digits **next to
each other** are counted as **a whole number** rather than separate digits.

### Examples

    grab_number_sum("aeiou250abc10") ➞ 260
    
    grab_number_sum("one1two2twenty20") ➞ 23
    
    grab_number_sum("900uwu50uwuuwuuwu25uwu25") ➞ 1000

### Notes

Remember not to just add _single digit numbers together_ , it should be
possible for answers to easily get into the 100s!

"""

def grab_number_sum(s):
    for c in s:
        if c.isalpha():
            s=s.replace(c," ")
    return sum(map(int, s.split()))

