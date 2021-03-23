"""


Create a function that returns `True` if there's at least one prime number in
the given range (`n1` to `n2` (inclusive)), `False` otherwise.

### Examples

    prime_in_range(10, 15) ➞ True
    # Prime numbers in range: 11, 13
    
    prime_in_range(62, 66) ➞ False
    # No prime numbers in range.
    
    prime_in_range(3, 5) ➞ True
    # Prime numbers in range: 3, 5

### Notes

  * `n2` is always greater than `n1`.
  * `n1` and `n2` are always positive.
  * 0 and 1 aren't prime numbers.

"""

def prime_in_range(n1, n2):
  
  Range = []
  
  Start = n1
  End = n2
  
  while (Start <= End):
    Range.append(Start)
    Start += 1
  
  Counter = 0
  Length = len(Range)
  
  while (Counter < Length):
    
    Value = Range[Counter]
    Factor = 1
    Factors = []
    
    while (Factor <= Value):
      
      if (Value % Factor == 0):
        Factors.append(Factor)
        Factor += 1
      else:
        Factor += 1
    
    Span = len(Factors)
    
    if (Span == 2):
      return True
    else:
      Counter += 1
        
  return False

