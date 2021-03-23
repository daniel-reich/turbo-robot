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
  lvl=0
  while True:
    lvl+=1
    runLst=[]
    for i in range(1,len(lst)):
      runLst.append(lst[i]-lst[i-1])
    if len(set(runLst))==1: break
    lst=runLst[:]
  if lvl==1: return 'Linear'
  if lvl==2: return 'Quadratic'
  if lvl==3: return 'Cubic'

