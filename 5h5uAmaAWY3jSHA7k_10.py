"""


A **mountain** is a list with **exactly one peak**.

  * All numbers to the left of the **peak** are increasing.
  * All numbers to the right of the **peak** are decreasing.
  * The peak CANNOT be on the boundary.

A **valley** is a list with **exactly one trough**.

  * All numbers to the left of the **trough** are decreasing.
  * All numbers to the right of the **trough** are increasing.
  * The trough CANNOT be on the boundary.

Some examples of **mountains** and **valleys** :

    Mountain A:  [1, 3, 5, 4, 3, 2]   # 5 is the peak
    Mountain B:  [-1, 0, -1]   # 0 is the peak
    Mountain B:  [-1, -1, 0, -1, -1]   # 0 is the peak (plateau on both sides is okay)
    
    Valley A: [10, 9, 8, 7, 2, 3, 4, 5]   # 2 is the trough
    Valley B: [350, 100, 200, 400, 700]  # 100 is the trough

Neither **mountains** nor **valleys** :

    Landscape A: [1, 2, 3, 2, 4, 1]  # 2 peaks (3, 4), not 1
    Landscape B: [5, 4, 3, 2, 1]  # Peak cannot be a boundary element
    Landscape B: [0, -1, -1, 0, -1, -1]  # 2 peaks (0)

Based on the rules above, write a function that takes in a list and returns
either `"mountain"`, `"valley"`, or `"neither"`.

### Examples

    landscape_type([3, 4, 5, 4, 3]) ➞ "mountain"
    
    landscape_type([9, 7, 3, 1, 2, 4]) ➞ "valley"
    
    landscape_type([9, 8, 9]) ➞ "valley"
    
    landscape_type([9, 8, 9, 8]) ➞ "neither"

### Notes

  * A **peak** is not exactly the same as the **max** of a list. The **max** is a unique number, but a list may have multiple peaks. However, if there exists only one peak in a list, then it is true that the peak = max.
  * See comments for a hint.

"""

def landscape_type(landscape):
    highestval = landscape[0]
    highestvallocation = 0
    for i in range(0, len(landscape)):
        if highestval < landscape[i]:
            highestval = landscape[i]
            highestvallocation = i
​
    if highestvallocation != 0 and highestvallocation != len(landscape)-1:
        lowerhalf = landscape[ : highestvallocation]
        higherhalf = landscape[highestvallocation+1 : ]
        check = 0
​
        for i in range(0, len(lowerhalf) - 1):
            if lowerhalf[i] > lowerhalf[i+1]:
                check = 1
​
        for i in range(0, len(higherhalf) - 1):
            if higherhalf[i] < higherhalf[i+1]:
                check = 1
    else:
        check = 1
​
    if check == 0:
        return "mountain"
    else:
        lowestval = landscape[0]
        lowestvallocation = 0
        for i in range(0, len(landscape)):
            if lowestval > landscape[i]:
                lowestval = landscape[i]
                lowestvallocation = i
​
        if lowestvallocation != 0 and lowestvallocation != len(landscape)-1:
            lowerhalf = landscape[ : lowestvallocation]
            higherhalf = landscape[lowestvallocation+1 : ]
            check = 0
​
            for i in range(0, len(lowerhalf) - 1):
                if lowerhalf[i] < lowerhalf[i+1]:
                    check = 1
​
            for i in range(0, len(higherhalf) - 1):
                if higherhalf[i] > higherhalf[i+1]:
                    check = 1
        else:
            check = 1
​
        if check == 0:
            return "valley"
        else:
            return "neither"

