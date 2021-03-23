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
  f_d = [lst[i]-lst[i-1] for i in range(1,len(lst))]
  s_d = [f_d[i]-f_d[i-1] for i in range(1,len(f_d))]
  t_d = [s_d[i]-s_d[i-1] for i in range(1,len(s_d))]
​
​
  return "Linear" if len(set(f_d)) == 1 else "Quadratic" if len(set(s_d)) == 1 else "Cubic"

