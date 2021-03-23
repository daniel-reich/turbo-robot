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

def is_palindrome(n):
  forward = str(n)
  backward = ''
  for i in range(len(forward)-1, -1, -1):
    backward += forward[i]
  if forward == backward:
    return True
  return False
​
def palindrome_descendant(n):
  all_descendants = [str(n)]
  while len(all_descendants[-1]) % 2 == 0:
    next_number = ''        
    for i in range(0, len(all_descendants[-1]), 2):
      next_number += str( int(all_descendants[-1][i]) + int(all_descendants[-1][i+1]) )
    all_descendants.append(next_number)
  for number in all_descendants:
    if is_palindrome(int(number)) and len(number) > 1.5:
      return True
  return False

