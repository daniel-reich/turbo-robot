"""


Traditional safes use a three-wheel locking mechanism, with the safe
combination entered using a dial on the door of the safe. The dial is marked
with clockwise increments between 0 and 99. The three-number combination is
entered by first dialling to the right (clockwise), then to the left (anti-
clockwise), and then to the right (clockwise) again. Combination numbers are
read from the top of the dial:

![](https://edabit-challenges.s3.amazonaws.com/image25.png)

Given the starting (top) position of the dial and the increments used for each
turn of the dial, return a list containing the _combination_ of the safe.

### Step-By-Step Example

    safecracker(0, [3, 10, 5]) ➞ [97, 7, 2]
    
    Starting dial position of 0 (same as the diagram above).
    
    First turn (rightward) of 3 increments:
    0 -> 99, 98, 97
    First number of combination = 97
    
    Second turn (leftward) of 10 increments:
    97 -> 98, 99, 0, 1, 2, 3, 4, 5, 6, 7
    Second number of combination = 7
    
    Third turn (rightward) of 5 increments:
    7 -> 6, 5, 4, 3, 2
    Third number of combination = 2
    
    The final combination is [97, 7, 2]

### Other Examples

    safecracker(96, [54, 48, 77]) ➞ [42, 90, 13]
    
    safecracker(43, [51, 38, 46]) ➞ [92, 30, 84]
    
    safecracker(4, [69, 88, 55]) ➞ [35, 23, 68]

### Notes

Each of the three combination numbers will be different.

"""

def safecracker(start, increments):
    combination = []
​
    count=0
​
    if start == 0:
        start = 100
    comb1 = start
    
    while increments[0] != count and start != 0 and comb1 !=0:
        comb1 = comb1-1 
        count=count+1
      
        if comb1 == 0:
            comb1 = 100
        if count == increments[0]:
       
            combination.append(comb1)
​
    
​
    count2=0
    if comb1 == 100:
        comb1 = 0
    comb2=comb1
    
    while increments[1] != count2 and comb2 != 100:
        comb2 = comb2 + 1
        count2 = count2+1
       
        if comb2 == 100:
            comb2 = 0
        if count2 == increments[1]:
            combination.append(comb2)
​
    count3=0
    if comb2 == 0:
        comb2 = 100
    comb3=comb2
    while increments[2] != count3 and comb3 != 0:
        comb3 = comb3-1
        count3 = count3+1
        if comb3 == 0:
            comb3 = 100
        if count3 == increments[2]:
            combination.append(comb3)
​
​
​
    return(combination)

