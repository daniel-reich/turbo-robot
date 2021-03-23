"""


Create a function that takes two integers and returns `true` if a digit
repeats three times in a row at any place in `num1` **AND** that same digit
repeats two times in a row in `num2`.

### Examples

    trouble(451999277, 41177722899) ➞ True
    
    trouble(1222345, 12345) ➞ False
    
    trouble(666789, 12345667) ➞ True
    
    trouble(33789, 12345337) ➞ False

### Notes

You can expect every test case to contain exactly two integers.

"""

def trouble(num1, num2):
  numlst1, numlst2 = list(str(num1)), list(str(num2))
  for i in range(len(numlst1)-2):
    if numlst1[i] == numlst1[i+1] == numlst1[i+2]:
      for j in range(len(numlst2)-1):
        if numlst2[j] == numlst2[j+1] == numlst1[i]:
          return True
        else: 
          continue
    else:
      continue
  return False

