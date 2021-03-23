"""


Write a function that will return `True` if a given string (divided and
grouped into a size) will contain a set of **consecutive** numbers (regardless
of orientation: whether **ascending** or **descending** ), otherwise, return
`False`.

### IMPORTANT

The expected solution for this challenge is done **recursively**. Please check
out the **Resources** tab for more details about **recursion** in Java.

### Examples

    is_consecutive("121314151617") ➞ True
    # Contains a set of consecutive ascending numbers
    # if grouped into 2's : 12, 13, 14, 15, 16, 17
    
    is_consecutive("123124125") ➞ True
    # Contains a set of consecutive ascending numbers
    # if grouped into 3's : 123, 124, 125
    
    is_consecutive("32332432536") ➞ False
    # Regardless of the grouping size, the numbers can't be consecutive.
    
    is_consecutive("326325324323") ➞ True
    # Contains a set of consecutive descending numbers
    # if grouped into 3's : 326, 325, 324, 323
    
    is_consecutive("667666") ➞ True
    # Consecutive descending numbers: 667 and 666.
    
    is_consecutive("999897959493") ➞ False

### Notes

  * A **number** can consist of any number of digits, so long as the numbers are **adjacent** to each other, and the string has **at least two** of them.
  * An **iterative** version of this challenge can be found via this [link](https://edabit.com/challenge/eHwd6medMrY3QXM8k).

"""

def is_consecutive(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
  
  if (len(Parameters) == 1):
    Parameters.append(1)
​
  Text = Parameters[0]
  Divider = Parameters[1]
  Length = len(Text)
  
  if (Divider == Length):
    return False
  else:
    
    Sample_A1 = Text
    Sample_A2 = Text[0:Divider]
    Number_A2 = int(Sample_A2) + 1
    
    Length_A1 = len(Sample_A1)
    Length_A2 = len(Sample_A2)
    
    while (Length_A2 < Length_A1):
      Sample_A2 = Sample_A2 + str(Number_A2)
      Number_A2 += 1
      Length_A1 = len(Sample_A1)
      Length_A2 = len(Sample_A2)
    
    Sample_B1 = Text
    Sample_B2 = Text[0:Divider]
    Number_B2 = int(Sample_B2) - 1
    
    Length_B1 = len(Sample_B1)
    Length_B2 = len(Sample_B2)
    
    while (Length_B2 < Length_B1):
      Sample_B2 = Sample_B2 + str(Number_B2)
      Number_B2 -= 1
      Length_B1 = len(Sample_B1)
      Length_B2 = len(Sample_B2)
    
    if (Sample_A1 == Sample_A2) or (Sample_B1 == Sample_B2):
      return True
    else:
      Divider += 1
      return is_consecutive(Text, Divider)

