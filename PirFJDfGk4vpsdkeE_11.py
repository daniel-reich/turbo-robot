"""


Bobby is troubleshooting a challenge he is attempting on Edabit. He needs to
devise a function whose argument is the size of a **square array**. The
function must return the array with the diagonals set to `1` and all the other
members set to `0`. His code is in the **Code** tab. Two of the lines contain
bugs. Can you help him?

### Examples

    help_bobby(1) ➞ [[1]]
    
    help_bobby(3) ➞ [
      [1, 0, 1],
      [0, 1, 0],
      [1, 0, 1]
    ]
    
    help_bobby(4) ➞ [
      [1, 0, 0, 1],
      [0, 1, 1, 0],
      [0, 1, 1, 0],
      [1, 0, 0, 1]
    ]

### Notes

N/A

"""

def help_bobby(size):
    l = []
    l2 = []
    t = 1
    for i in range(size):
        for j in range(size):
           l.append(t)
           t += 1
        l2.append(l)
        l = []
    s = size
    for i in range(size):
        l2[i][i] = 1
        l2[i][s-1] = 1
        s-=1
        for j in range(len(l2[i])):
            if l2[i][j] !=1:
                l2[i][j] = 0
    return l2

