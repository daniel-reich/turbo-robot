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

def seq(lst):
  konar=[]
  for i in range(len(lst[:-1])):
    konar.append(lst[i+1]-lst[i])
  return konar
def same(lst):
  return lst[1:][0]==lst[0]
​
def seq1(lst):
  if same(lst):
    return 0
  else:
    return 1+seq1(seq(lst))
    
def seq_level(lst):
  num=seq1(lst)
  if num==1:
    return 'Linear'
  elif num==2:
    return 'Quadratic'
  elif num==3:
    return "Cubic"

