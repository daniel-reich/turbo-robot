"""


A number is Zygodrome if can be partitioned into clusters of repeating digits
with a length equals or greater than two (as to say that repeating digits need
to be placed as an adjacent pair or a greater group, and that no single digits
are allowed).

Given a non-negative integer `num`, implement a function that returns `True`
if `num` is a Zygodrome number, or `False` otherwise.

### Examples

    is_zygodrome(11) ➞ True
    # 11 is a pair of repeated digits
    
    is_zygodrome(33322) ➞ True
    # 333 is a triplet of repeated digits, and 22 is a pair
    
    is_zygodrome(5) ➞ False
    # 5 is a single digit, it doesn't form a pair
    
    is_zygodrome(1001) ➞ False
    # 00 is a pair, but the two 1's are not adjacent

### Notes

  * Trivia: the number `9997777` is the only known Zygodrome prime whose index in the Zygodromes sequence (`664444`) is a prime in turn.
  * You can expect only non-negative integers as given input, without exceptions to handle.

"""

def is_zygodrome(num):
  s = str(num)
  if len(s) < 2 or s[0] != s[1] or s[-1] != s[-2]:
    return False
  for x in range(1, len(s)-2):
    if s[x] != s[x-1] and s[x] != s[x+1]:
      return False
  return True

