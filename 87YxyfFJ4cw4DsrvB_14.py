"""


Create a function that takes in parameter `n` and generates an `n x n` (where
`n` is odd) **concentric rug**.

The center of a concentric rug is `0`, and the rug "fans-out", as show in the
examples below.

### Examples

    generate_rug(1) ➞ [
      [0]
    ]
    
    generate_rug(3) ➞ [
      [1, 1, 1],
      [1, 0, 1],
      [1, 1, 1]
    ]
    
    generate_rug(5) ➞ [
      [2, 2, 2, 2, 2],
      [2, 1, 1, 1, 2],
      [2, 1, 0, 1, 2],
      [2, 1, 1, 1, 2],
      [2, 2, 2, 2, 2]
    ]
    
    generate_rug(7) ➞ [
      [3, 3, 3, 3, 3, 3, 3],
      [3, 2, 2, 2, 2, 2, 3],
      [3, 2, 1, 1, 1, 2, 3],
      [3, 2, 1, 0, 1, 2, 3],
      [3, 2, 1, 1, 1, 2, 3],
      [3, 2, 2, 2, 2, 2, 3],
      [3, 3, 3, 3, 3, 3, 3]
    ]

### Notes

  * `n >= 0`.
  * Always increment by 1 each "layer" outwards you travel.

"""

def generate_rug(n):
    retLst =[]
    intialNumber = int((n-1)/2)
    
    for i in range(intialNumber):
        row = []
        for j in range(i+1):
            row.append(intialNumber-j)
        loopForIntN = n - ((i+1)*2)
        if loopForIntN > 0:
            for j in range(loopForIntN):
                row.append(intialNumber-i)
        for j in range(intialNumber-i,intialNumber+1):
            row.append(j)
        
        retLst.append(row)
        
    #copy
    restLst = retLst.copy()
    restLst.reverse()
    
    #centerRow
    row=[]
    for i in range(n):
        v = abs(i- intialNumber)
        row.append(v)
    retLst.append(row)
    retLst.extend(restLst)
        
    
    return retLst

