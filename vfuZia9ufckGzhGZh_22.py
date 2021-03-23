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
  difference = lambda x: [x[foo + 1] - x[foo] for foo in range(len(x) - 1)]
  return_lst = ["Linear", "Quadratic", "Cubic"]
  
  for bar in range(3):
    lst = difference(lst)
    if len(set(lst)) == 1:
      return return_lst[bar]
  return None

