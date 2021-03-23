"""


Write a function that returns the greatest common divisor of all list
elements. If the greatest common divisor is `1`, return `1`.

### Examples

    GCD([10, 20, 40]) ➞ 10
    
    GCD([1, 2, 3, 100]) ➞ 1
    
    GCD([1024, 192, 2048, 512]) ➞ 64

### Notes

  * List elements are always greater than `0`.
  * There is a minimum of two list elements given.

"""

def GCD(lst):
  
  Answer = 1
  
  Test = 2
  End = min(lst)
  
  while (Test <= End):
    
    Outcomes = []
    
    Counter = 0
    Length = len(lst)
    
    while (Counter < Length):
      Number = lst[Counter]
      Outcome = Number % Test
      Outcomes.append(Outcome)
      Counter += 1
    
    Outcomes = set(Outcomes)
    Outcomes = list(Outcomes)
    
    if (Outcomes == [0]):
      Answer = Test
      Test += 1
    else:
      Test += 1
  
  return Answer

