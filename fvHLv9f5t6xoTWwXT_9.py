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
    sum_nums = 0
    begin = -1
    for i, c in enumerate(s):
        if c.isdigit() and begin < 0:
            begin = i
        elif not c.isdigit() and begin >= 0:
            sum_nums += int(s[begin: i])
            begin = -1
        elif c.isdigit() and i == len(s) - 1:
            sum_nums += int(s[begin: i + 1])
    return sum_nums

