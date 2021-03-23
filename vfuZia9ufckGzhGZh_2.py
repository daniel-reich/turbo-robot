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
  dif1 = [j - i for i, j in zip(lst, lst[1:])]
  dif2 = [j - i for i, j in zip(dif1, dif1[1:])]
  dif3 = [j - i for i, j in zip(dif2, dif2[1:])]
  
  if not sum(dif2) : return 'Linear'
  if not sum(dif3) : return 'Quadratic'
  return 'Cubic'

