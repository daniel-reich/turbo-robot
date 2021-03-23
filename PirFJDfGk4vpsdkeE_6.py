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
    array=[a for a in [[0]*size for _ in range(size)]]
    for column in range(size):
        array[column][column]=1
        array[size - column - 1][column]=1
    for i in array:print(i)
    return array

