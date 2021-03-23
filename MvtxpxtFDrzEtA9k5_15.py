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

def palindrome_descendant(num):
  s_num = str(num)
  l = len(s_num)
  if s_num == s_num[::-1]:
    return True
  if l == 2:
    return False
  if (l % 2) != 0:
    s_num += '0'
  new_num = ''
  while l > 0:
    new_num += str(int(s_num[0]) + int(s_num[1]))
    s_num = s_num[2:]
    l -= 2
  return palindrome_descendant(new_num)

