"""


Create a function to rotate a two-dimensional matrix of `N * N` integer
elements `num` times, where if `num` is positive, the rotation is
**clockwise** , and if not, **counterclockwise**.

### Examples

    rotate_transform([
      [2, 4],
      [0, 0]
    ], 1) ➞ [
      [0, 2],
      [0, 4]
    ]
    rotate_transform([
      [2, 4],
      [0, 0]
    ], -1) ➞ [
      [4, 0],
      [2, 0]
    ]

### Notes

N/A

"""

def rotate_transform(arr, num):
  if num%4==0: return arr
  for cycl in range(num%4):
    newM=[['']*len(arr) for j in range(len(arr[0]))]
    newI=[]
    i=0
    for cl in range(len(arr)-1,-1,-1):
      for ro in range(len(arr[0])):
        newI=newI + [ro] + [cl]
    for row in arr:
      for val in row:
        newM[newI[i]][newI[i+1]]=val
        i+=2
    arr=newM  
  return newM

