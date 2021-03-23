"""


Create a function that takes a list of 10 numbers (between 0 and 9) and
returns a string of those numbers formatted as a phone number (e.g. **(555)
555-5555** ).

### Examples

    format_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) ➞ "(123) 456-7890"
    
    format_phone_number([5, 1, 9, 5, 5, 5, 4, 4, 6, 8]) ➞ "(519) 555-4468"
    
    format_phone_number([3, 4, 5, 5, 0, 1, 2, 5, 2, 7]) ➞ "(345) 501-2527"

### Notes

Don't forget the space after the closing parenthesis.

"""

def format_phone_number(lst):
    first, mid, last = '', '', ''
    for num in lst:
        if len(first) <= 2:
            first += str(num)
        elif len(mid) <= 2 and len(first) == 3:
            mid += str(num)
        elif len(mid) <= 3 and len(first) <= 3 and len(last) <= 3:
            last += str(num)
    string = '(%s) %s-%s' % (first, mid, last)
    return string
