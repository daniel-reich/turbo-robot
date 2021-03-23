"""


Create a function that determines if a given sequence is _linear_ ,
_quadratic_ or _cubic_. The input will be a list of numbers of varying
lengths. The function should return `"Linear"`, `"Quadratic"` or `"Cubic"`.

### Examples

    seq_level(1, 2, 3, 4, 5) ➞ "Linear"
    
    seq_level(3, 6, 10, 15, 21) ➞ "Quadratic"
    
    seq_level(4, 14, 40, 88, 164) ➞ "Cubic"

### Notes

N/A

"""

def seq_level(lst):
  if lst[1]-lst[0] == lst[2]-lst[1]:
    return "Linear"
  elif lst[3] - (2*lst[2]) + lst[1] == lst[2] - (2*lst[1]) + lst[0]:
    return "Quadratic"
  else:
    return "Cubic"

