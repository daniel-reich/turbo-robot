"""


Write a function that, given the `start` and `end` values, returns an array
containing all the numbers **inclusive** to that range. See examples below.

### Examples

    reversible_inclusive_list(1, 5) ➞ [1, 2, 3, 4, 5]
    
    reversible_inclusive_list(2, 8) ➞ [2, 3, 4, 5, 6, 7, 8]
    
    reversible_inclusive_list(10, 20) ➞ [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    
    reversible_inclusive_list(24, 17) ➞ [24, 23, 22, 21, 20, 19, 18, 17]

### Notes

  * The sort order of the resulting array is dependent of the input values.
  * All inputs provided in the test scenarios are valid.
  * If `start` is greater than `end`, return a **descendingly** sorted array, otherwise, **ascendingly** sorted.
  * You are expected to solve this challenge via a **recursive** approach.
  * An iterative version of this challenge can be found via this [link](https://edabit.com/challenge/zW9JME7XNew4tgCCE).

"""

def reversible_inclusive_list(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
    
  if (len(Parameters) == 2):
    Parameters.append([])
    Parameters.append(Parameters[0])
    Parameters.append(0)
  
  Start = Parameters[0]
  End = Parameters[1]
  Answer = Parameters[2]
  Cursor = Parameters[3]
  Added = Parameters[4]
  Required = abs(Start - End) + 1
  
  if (Added == Required):
    return Answer
  
  elif (Added < Required) and (Start > End):
    Answer.append(Cursor)
    Added += 1
    Cursor -= 1
    return reversible_inclusive_list(Start, End, Answer, Cursor, Added)
  
  elif (Added < Required) and (Start < End):
    Answer.append(Cursor)
    Added += 1
    Cursor += 1
    return reversible_inclusive_list(Start, End, Answer, Cursor, Added)
  
  else:
    return "ERROR"

