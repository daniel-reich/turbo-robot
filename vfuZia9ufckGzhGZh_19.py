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

def differences(lst):
  return [lst[i] - lst[i - 1] for i in range(1, len(lst))]
​
def seq_level(lst):
  res = ["Linear", "Quadratic", "Cubic"]
  diff = differences(lst)
  level = 0
  while len(set(diff)) > 1:
    diff = differences(diff)
    level += 1
  return res[level]

