"""


A number may not be a palindrome, but its descendant can be. A number's direct
child is created by summing each pair of adjacent digits to create the digits
of the next number.

For instance, `123312` is not a palindrome, but its next child `363` is,
where: `3 = 1 + 2; 6 = 3 + 3; 3 = 1 + 2`.

Create a function that returns `True` if the **number itself** is a palindrome
or any of its **descendants down to 2 digits** (a 1-digit number is trivially
a palindrome).

### Examples

    palindrome_descendant(11211230) ➞ True
    # 11211230 ➞ 2333 ➞ 56 ➞ 11
    
    palindrome_descendant(13001120) ➞ True
    # 13001120 ➞ 4022 ➞ 44
    
    palindrome_descendant(23336014) ➞ True
    # 23336014 ➞ 5665
    
    palindrome_descendant(11) ➞ True
    # Number itself is a palindrome

### Notes

Numbers will always have an even number of digits.

"""

def palindrome_descendant(n):
    '''
    Returns True if the digits in n or its descendants down to 2 digits derived
    as above are.
    '''
    str_n = str(n)
    
    if str_n == str_n[::-1] and len(str_n) != 1:
        return True
​
    if len(str_n) % 2 == 1:
        return False  # Cannot produce a full set of pairs
​
    
    return palindrome_descendant(int(''.join(str(int(str_n[i]) + int(str_n[i+1])) \
                                     for i in range(0, len(str_n), 2))))

