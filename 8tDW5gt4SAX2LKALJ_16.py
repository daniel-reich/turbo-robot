"""


This is a sequel to [Chain Reaction (Part
#1)](https://edabit.com/challenge/bf3QRDxH9Ns2SZWZw), with the same setup, but
a different flavor.

As in the previous part, you will be given a rectangular array representing a
"map" with three types of spaces:

  * "+" bombs: when activated, their explosion activates any bombs directly above, below, left, or right of the "+" bomb.
  * "x" bombs: when activated, their explosion activates any bombs placed in any of the four diagonal directions next to the "x" bomb.
  * Empty spaces "0".

The goal is simple: **given a map, return the minimum number of bombs that
need to be set off for all bombs to be destroyed by the chain reaction**.

Let's look at some examples:

    [
      ["+", "+", "+", "0", "+", "+", "+"],
      ["+", "+", "+", "0", "0", "+", "+"]
    ]

For the map above, the answer is `2`; to explode all bombs you just need to
set off one "+" bomb in the right cluster and one in the left cluster.

    [
      ["x", "0", "x"],
      ["x", "x", "x"]
    ]

For the map above, the answer is `3`; clearly setting off the three bottom "x"
bombs is enough, and no less than three bombs suffice.

    [
      ["x", "x", "x", "0", "x"],
      ["x", "x", "x", "x", "x"],
      ["x", "x", "x", "0", "x"]
    ]

For the map above, the answer is `3`; setting off the three rightmost bombs in
the middle row will do the trick.

### Examples

    min_bombs_needed([
      ["+", "+", "+", "0", "+", "+", "+"],
      ["+", "+", "+", "0", "0", "+", "+"]
    ]) ➞ 2
    
    min_bombs_needed([
      ["x", "0", "x"],
      ["x", "x", "x"]
    ]) ➞ 3
    
    min_bombs_needed([
      ["x", "x", "x", "0", "x"],
      ["x", "x", "x", "x", "x"],
      ["x", "x", "x", "0", "x"]
    ]) ➞ 3

### Notes

  * Note that both "+" and "x" bombs have an "explosion range" of 1.
  * To limit the difficulty, in this challenge each map will have only "+" or only "x" bombs. The more challenging case of maps with both "+" and "x" bombs will be [part 3](https://edabit.com/challenge/LLieA2XafALFxXRT5)!
  * Figuring out what to do is half the fun, but if you'd prefer to just handle the coding, a hint on to how to attack this challenge can be found in the comments.

"""

from functools import reduce
def reachable_bombs(m):
   r=[[set() for col in range(len(m[0]))] for row in range(len(m))]
   for i in range(len(m)):
     for j in range(len(m[0])):
       if m[i][j] == '+':
         r[i][j]=set([len(m[0])*i+j]+list((r[i-1][j] if i>0 else []))+list((r[i][j-1] if j>0 else []))+reachables(m,(i,j+1))+reachables(m,(i+1,j)))
       if m[i][j] == 'x':
         r[i][j]=set([len(m[0])*i+j]+list((r[i-1][j-1] if i>0 and j>0 else []))+list((r[i-1][j+1] if i>0 and j<len(m[0])-1 else []))+reachables(m,(i+1,j-1))+reachables(m,(i+1,j+1)))
   rb=[[set() for col in range(len(m[0]))] for row in range(len(m))]
   for i in range(len(m)):
     for j in range(len(m[0])):
       for k in r[i][j]:
           rb[i][j]=rb[i][j]|r[k//len(m[0])][k%len(m[0])]
   return rb
​
def reachables(m,t):
   i,j=t
   if i<0 or i>len(m)-1:
      return []
   if j<0 or j>len(m[0])-1:
      return []
   if m[i][j] == '0':
      return []
   if m[i][j] == '+':
      return [len(m[0])*i+j]+reachables(m,(i,j+1))+reachables(m,(i+1,j))
   if m[i][j] == 'x':
      return [len(m[0])*i+j]+reachables(m,(i+1,j-1))+reachables(m,(i+1,j+1))
​
def min_bombs_needed(m):
   bombs=[]
   for i in range(len(m)):
       for j in range(len(m[0])):
           bombs=bombs+[i*len(m[0])+j] if m[i][j]=='+' or m[i][j]=='x' else bombs
   bs=set(bombs)
   rb=reachable_bombs(m)
   rbs=reduce(lambda x,y: x+y, rb, [])
   rbs=set(map(lambda x: frozenset(x), rbs))
   rbs=sorted(rbs,key=len,reverse=True)
   s=set()
   c=0
   for i in range(len(rbs)):
      if not rbs[i]&s==rbs[i]:
         c+=1
         s=s|rbs[i]
      if s==bs:
        break
   return c

