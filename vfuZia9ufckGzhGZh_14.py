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

def get_level(lst):
  l = [lst[i] - lst[i-1] for i in range(1,len(lst))]
  return 1 + get_level(l) if sum(l) != 0 else 0
​
def seq_level(lst):
  d = ["Linear","Quadratic","Cubic"]
  return d[get_level(lst)-1]

