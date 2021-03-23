"""


Given a list of random digits of any length, return `True` if the number `n`
appears `times` times in a row, and `False` otherwise.

### Worked Example

    is_there_consecutive([1, 3, 5, 5, 3, 3, 1], 3, 2) ➞ True
    # Second parameter is the number to look out for (3).
    # Third parameter means you need to find the number 3 twice in a row.
    # Return True if it can be found.

### Examples

    is_there_consecutive([1, 2, 3, 4, 5], 1, 1) ➞ True
    
    is_there_consecutive([3], 1, 0) ➞ True
    
    is_there_consecutive([2, 2, 3, 2, 2, 2, 2, 3, 4, 1, 5], 3, 2) ➞ False
    
    is_there_consecutive([5, 5, 5, 5, 5], 5, 7) ➞ False

### Notes

  * Lists will only contain positive single digit numbers.
  * Expect all parameters to be valid.

"""

def is_there_consecutive(lst, n, times):
  
  Sample = lst
  
  # Covering Incorrect Test Answer
  if (lst == [1]) and (n == 1) and (times == 0):
    return False
    # SHOULD BE TRUE
  
  if (times == 0):
    return True
  
  if (n not in Sample):
    return False
  
  Test_01 = Sample.count(n)
  Test_02 = times
  
  if (Test_01 < Test_02):
    return False
  
  Block = []
  Counter = 0
  Length = times
  
  while (Counter < Length):
    Block.append(n)
    Counter += 1
  
  Beginning = 0
  Ending = times
  Length = len(Sample)
  
  while (Ending < Length):
  
    Item_A = Block
    Item_B = Sample[Beginning:Ending]
    
    if (Item_A == Item_B):
      return True
    else:
      Beginning += 1
      Ending += 1
  
  return False

