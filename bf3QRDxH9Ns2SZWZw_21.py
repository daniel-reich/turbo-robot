"""


In this challenge you will be given a rectangular list representing a "map"
with three types of spaces:

  *  **"+" bombs:** When activated, their explosion activates any bombs directly above, below, left, or right of the "+" bomb.
  *  **"x" bombs:** When activated, their explosion activates any bombs placed in any of the four diagonal directions next to the "x" bomb.
  * Empty spaces "0".

Consider the grid:

    [
      ["+", "+", "0", "x", "x", "+", "0"],
      ["0", "+", "+", "x", "0", "+", "x"]
    ]

If the top left "+" bomb explodes, the resulting chain reaction will blow up
bombs in the order given by the numbers below:

    [
      ["1", "2", "0", "x", "6", "8", "0"],
      ["0", "3", "4", "5", "0", "7", "8"]
    ]

Note that there are two 8's since two of the bombs explode at the same time.
Also, note that one of the "x" bombs in the top row does not explode.

Write a function that determines if the chain reaction started when the _top
left bomb_ explodes destroys all bombs or not.

### Examples

    all_explode([
      ["+", "+", "+", "+", "+", "+", "x"]
    ]) ➞ True
    
    all_explode([
      ["+", "+", "+", "+", "+", "0", "x"]
    ]) ➞ False
    
    all_explode([
      ["+", "+", "0", "x", "x", "+", "0"],
      ["0", "+", "+", "x", "0", "+", "x"]
    ]) ➞ False
    
    all_explode([
      ["x", "0", "0"],
      ["0", "0", "0"],
      ["0", "0", "x"]
    ]) ➞ False
    
    all_explode([
      ["x", "0", "x"],
      ["0", "x", "0"],
      ["x", "0", "x"]
    ]) ➞ True

### Notes

  * Both "+" and "x" bombs have an "explosion range" of 1.
  * Part #2 can be [found here](https://edabit.com/challenge/8tDW5gt4SAX2LKALJ).

"""

def all_explode(lst):
  A=[(i,j) for i in range(len(lst)) for j in range(len(lst[0]))]
  P=[x for x in A if lst[x[0]][x[1]]=='+']
  X=[x for x in A if lst[x[0]][x[1]]=='x']
  d1={p:[] for p in P}
  for p in P:
    for a in A:
      if p!=a and (abs(p[0]-a[0])==1 and p[1]==a[1]) or (abs(p[1]-a[1])==1 and p[0]==a[0]):
        if lst[a[0]][a[1]]!='0':
          d1[p].append(a)
  d2={x:[] for x in X}
  for x in X:
    for a in A:
      if x!=a and (abs(x[0]-a[0])==1 and abs(x[1]-a[1])==1):
        if lst[a[0]][a[1]]!='0':
          d2[x].append(a)
  d1.update(d2)
  qu=[(0,0)]
  done={(0,0)}
  res=[]
  while qu:
    k=qu.pop(0)
    res.append(k)
    for x in d1[k]:
      if x not in done:
        qu.append(x)
        done.add(x)
  return len(P)+len(X)==len(res)

