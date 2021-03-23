"""


Write a function that extracts the max value of a number in a list. If there
are **two or more** max values, return it **as a list** , otherwise, return
the **number**. This process could be relatively easy with some of the built-
in list functions but the required approach is **recursive**.

### Examples

    iso_group([31, 7, 2, 13, 7, 9, 10, 13]) ➞ 31
    
    iso_group([1, 3, 9, 5, 1, 7, 9, -9]) ➞ [9, 9]
    
    iso_group([97, 19, -18, 97, 36, 23, -97]) ➞ [97, 97]
    
    iso_group([-31, -7, -13, -7, -9, -13]) ➞ [-7, -7]
    
    iso_group([-1, -3, -9, -5, -1, -7, -9, -9]) ➞ [-1, -1]
    
    iso_group([107, 19, -18, 79, 36, 23, 97]) ➞ 107

### Notes

You can read more about recursion (see the **Resources** tab) if you aren't
familiar with it yet or haven't fully understood the concept before taking up
this challenge.

"""

def iso_group(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
    
  if (len(Parameters) == 1):
    Answer = []
    Answer.append(-999999)
    Parameters.append(Answer)
  
  Sample = Parameters[0]
  Answer = Parameters[1]
  
  if (Sample == []) and (len(Answer) == 1):
    return Answer[0]
  
  elif (Sample == []) and (len(Answer) > 1):
    return Answer
  
  elif (Sample[0] > Answer[0]):
    Answer = []
    Answer.append(Sample[0])
    return iso_group(Sample[1:], Answer)
  
  elif (Sample[0] == Answer[0]):
    Answer.append(Sample[0])
    return iso_group(Sample[1:], Answer)
  
  else:
    return iso_group(Sample[1:], Answer)

