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
    number = n//2
    roundednumber = number +1
    a = number
    counter = 0
    list1 = []
    for i in range(n):
        list1.append('')
    for i in range(roundednumber):
        if a == 0:
            list1[number] = 0
            break
        (list1[counter],list1[(counter*-1)-1]) = a,a
        a-=1
        counter+=1
            
    howmanyleft = 0
    emptylist = list1.copy()
    list1 =[]
    list1.insert(0,emptylist)
            
    for i in range(number):
        emptylist = emptylist.copy()
        print(howmanyleft)
        for i in range(howmanyleft+1):
            (emptylist[number-i],emptylist[number+i]) = emptylist[number-i]+1,emptylist[number-i]+1
        
        list1.insert(0,emptylist)
        list1.append(emptylist)    
        howmanyleft+=1
    
        if howmanyleft >number:
            break
​
    return list1

