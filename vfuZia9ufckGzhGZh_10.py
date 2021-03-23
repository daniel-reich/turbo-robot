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
  def transfo(l):
    return [l[i+1]-l[i] for i in range(len(l)-1)]
  n=1
  lst=transfo(lst)
  while len(set(lst))!=1:
    lst=transfo(lst)
    n+=1
  return {1: 'Linear', 2: 'Quadratic', 3: 'Cubic'}[n]

