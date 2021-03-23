"""


Create a function that takes in **size** and **direction** and generates a
**diagonal rug**.

The size is the `n` parameter, and all rugs are square `n x n`. The direction
is whether the diagonal part begins on the left or the right side.

### Examples

    generate_rug(4, "left") ➞ [
      [0, 1, 2, 3],
      [1, 0, 1, 2],
      [2, 1, 0, 1],
      [3, 2, 1, 0]
    ]
    
    generate_rug(5, "right") ➞ [
      [4, 3, 2, 1, 0],
      [3, 2, 1, 0, 1],
      [2, 1, 0, 1, 2],
      [1, 0, 1, 2, 3],
      [0, 1, 2, 3, 4]
    ]
    
    generate_rug(1, "left") ➞ [
      [0]
    ]
    
    generate_rug(2, "right") ➞ [
      [1, 0],
      [0, 1]
    ]

### Notes

  * `n > 0`
  * A `1 x 1` rug is trivially `[[0]]` (same for left and right).

"""

def generate_rug(n, direction):
  if direction=="left":
    l=[]
    e=[]
    ml=[]
    switch=True
    for i in range(n):
      l.append(i)
    ml.append(l)
    while(True):
      if len(e)>0:
        ml.append(e)
        switch=True
        l=list(e)
        e=[]
      if len(ml)==n:
        return ml
      for r in l:
        if r==0:
          switch=False
          e.append(r+1)
        else:
          if switch==False:
            e.append(r-1)
          else:
            e.append(r+1)
  if direction=="right":
    l=[]
    e=[]
    ml=[]
    switch=True
    for i in range(n):
      l.append(i)
    l.sort(reverse=True)
    ml.append(l)
    while(True):
      if len(e)>0:
        ml.append(e)
        switch=True
        l=list(e)
        e=[]
      if len(ml)==n:
        return ml
      for r in l:
        if r-1==0:
          if switch==False:
            e.append(r+1)
          else:
            switch=False
            e.append(r-1)
        else:
          if switch==False:
            e.append(r+1)
          else:
            e.append(r-1)

