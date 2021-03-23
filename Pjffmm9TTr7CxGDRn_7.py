"""


Write a function that will return `True` if a given string (divided and
grouped into a size) will contain a set of **consecutive ascending** numbers,
otherwise, return `False`.

### IMPORTANT

The expected solution for this challenge is done **recursively**. Please check
out the **Resources** tab for more details about **recursion** if it needs be.

### Examples

    is_ascending("123124125") ➞ True
    # Contains a set of consecutive ascending numbers
    # if grouped into 3's : 123, 124, 125
    
    is_ascending("101112131415") ➞ True
    # Contains a set of consecutive ascending numbers
    # if grouped into 2's : 10, 11, 12, 13, 14, 15
    
    is_ascending("32332432536") ➞ False
    # Regardless of the grouping size, the numbers can't be consecutive.
    
    is_ascending("326325324323") ➞ False
    # Though the numbers (if grouped into 3's) are consecutive but descending.
    
    is_ascending("666667") ➞ True
    # Consecutive numbers: 666 and 667.

### Notes

  * A **number** can consist of any number of digits, so long as the numbers are **adjacent to each other** , and the string has **at least two** of them.
  * An **iterative** version of this challenge can be found via this [link](https://edabit.com/challenge/LMoP4Jhpm9kx4WQ3a).

"""

def is_ascending(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
    
  if (len(Parameters) == 1):
    Parameters.append(1)
    
  Text = Parameters[0]
  Divider = Parameters[1]
  Ceiling = len(Text) - 1
  
  if (Divider == Ceiling):
    return False
  
  else:
    
    Sample_A = Text
    Sample_B = Text[0:Divider]
    
    Number = int(Sample_B) + 1
    
    Length_A = len(Sample_A)
    Length_B = len(Sample_B)
    
    while (Length_B < Length_A):
      Sample_B = Sample_B + str(Number)
      Number += 1
      Length_A = len(Sample_A)
      Length_B = len(Sample_B)
    
    if (Sample_A == Sample_B):
      return True
    else:
      Divider += 1
      return is_ascending(Text, Divider)

