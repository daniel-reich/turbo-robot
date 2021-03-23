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
  seq = lambda x:[b-a for a,b in zip(x,x[1:])]
  is_linear = lambda x:len(set(seq(x))) == 1
  
  return 'Linear' if is_linear(lst)\
    else 'Quadratic' if is_linear(seq(lst))\
    else 'Cubic'

