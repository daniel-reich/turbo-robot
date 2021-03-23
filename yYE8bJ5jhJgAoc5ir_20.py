"""


Create a function that takes an integer and returns its **multiplicative
persistence** , which is the number of times you must multiply the digits in
`num` until you reach a single digit.

### Examples

    bugger(39) ➞ 3
    # Because 3 * 9 = 27, 2 * 7 = 14, 1 * 4 = 4 and 4 has only one digit.
    
    bugger(999) ➞ 4
    # Because 9 * 9 * 9 = 729, 7 * 2 * 9 = 126, 1 * 2 * 6 = 12, and finally 1 * 2 = 2.
    
    bugger(4) ➞ 0
    # Because 4 is already a one-digit number.

### Notes

N/A

"""

def bugger(num):
    count = 0
    while len(str(num)) > 1:
        num = str(num)
        new_num = 1
        for char in num:
            new_num *= int(char)
        num = new_num
        count += 1
    
    return count

