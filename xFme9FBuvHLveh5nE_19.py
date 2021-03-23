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
  if num < 10: return False
  car, *cdr  = str(num)
  for i in cdr:
    if i in car:
      car += i
    else:
      if len(car) < 2:
        return False
      else:
        car = i
  return True if len(car) > 1 else False

