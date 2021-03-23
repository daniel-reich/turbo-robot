"""


Create a function that checks if the given arguments are of the same type.
Return `True` if they are and `False` if they're not.

### Examples

    compare_data(1, 6, 5, 3, 7, 9) ➞ True
    
    compare_data(1, 6, 5, 3, "7", 9) ➞ False
    
    compare_data([]) ➞ True
    
    compare_data([1], (1)) ➞ False

### Notes

  * If no input is given or only one input, return `True`.
  * Use the (*args) construct to enter an undefined number of function arguments.

"""

def compare_data(*args):
  print(args)
  t = True
  for i in range(len(args)):
    if isinstance(args[i], type(args[0])):
      pass
    else:
      t = False
      print("boop")
      break
  return t

