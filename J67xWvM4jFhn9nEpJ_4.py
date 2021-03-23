"""


Make a function that takes a integer, `size`, returns 2D list that is a Magic
Square with side lengths of `size`

A Magic Square is an arrangement of numbers in a square in such a way that the
sum of each row, column, and diagonal is one constant number, the "magic
constant." For this challenge I will be testing with the assumption that your
magic squares are made with whole numbers from 1 - n^2

### Example

    make_magic(3) ➞ [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    # Rows: 2+7+6 = 9+5+1 = 4+3+8 = 15
    # Columns: 2+9+4 = 7+5+3 = 6+1+8 = 15
    # Diagonals: 2+5+8 = 6+5+4 = 15

### Notes

For this challenge I will only be testing with sizes >= 3 as there are no
Magic Squares of size 2 at least as I have described them.

"""

#~~~~~~~~~~~~~~~~Testing_Function~~~~~~~~~~~~~~~~~~~~
def isMagic(square):
    size = len(square)
    magicNum =  (size**3 + size)/2
    # check rows:
    for row in square:
                    if sum(row) != magicNum or len(row) != size:
                                    return False  
    # check columns:
    for col in range(size):
                    column = [square[row][col] for row in range(size)]
                    if sum(column) != magicNum:
                                    return False
                                    
    # check diagonals:
    if sum([square[i][i] for i in range(size)]) != magicNum:
                    return False
    if sum([square[i][(size-1)-i] for i in range(size)]) != magicNum:
                    return False
                    
    # It must be magical then
    return True
​
#--------------------------------------------------------------
'''
Print contents of 2d array
'''
def printArray(array):
    print('Array...')
    for row in array:
        print('[', end = '')
        for v in row:
            s = '{0:4d}'.format(v)
            print(s, end = '')
        print(']')
        
​
#--------------------------------------------------------------
'''
Do one step of array swap process
'''
def swapOneArray(arr1, arr2, ra1, ra2, rb1, c1, c2):
    rb = rb1
    for ra in range(ra1, ra2 + 1):
        cb = c1
        for ca in range(c1, c2 + 1):
            arr2[rb][cb] = arr1[ra][ca]
            cb += 1
        rb += 1
    
#--------------------------------------------------------------
'''
Perform array swap in three steps
    First swap region 1 to temp array
    Second swap region 2 to region 1
    Third swap temp array to region 2
'''
def swapArrays(arr, ra1, ra2, rb1, rb2, c1, c2):
    size = len(arr)
    tmp = [[-1 for i in range(size)] for j in range(size)]
    swapOneArray(arr, tmp, ra1, ra2, rb1, c1, c2)
    swapOneArray(arr, arr, rb1, rb2, ra1, c1, c2)
    swapOneArray(tmp, arr, rb1, rb2, rb1, c1, c2)
            
#--------------------------------------------------------------
'''
Make odd magic square from whole or portion of a 2D array
    arr - Complete array - empty positions initalized with -1
    lims - row/columns inclusive to include
    start - Start count value
'''
def makeOdd(arr, lims, start):
​
    # Row/columns, max count for loop, initial row/column
    r1, r2, c1, c2 = lims
    max = start + (r2 - r1 + 1) ** 2
    r = r1
    c = c1 + ((c2 - c1)// 2)
​
    # Working row/column, start value, set initial position
    rp = cp = 0
    val = start
    arr[r][c] = val
​
    #Compute working row/column based on magic square logic
    for i in range(start, max-1):
        val += 1
        if( ((r-1) < r1) and ((c+1) > c2)):
            rp = r + 1
            cp = c
        elif((r-1) < r1):
            rp = r2
            cp = c+1
        elif((c+1) > c2):
            rp = r-1
            cp = c1
        else:
            rp = r-1
            cp = c+1
        if(arr[rp][cp] != -1):
            rp = r+1
            cp = c
​
        arr[rp][cp] = val
        r = rp
        c = cp
​
    # Return computed magic square region and starting value for
    # next magic square
    return (arr, val + 1)
    
#--------------------------------------------------------------
'''
Make single even magic square from whole part of a 2D array
(size divisable by 2 but not 4)
    arr - Complete array - empty positions initalized with -1
    start - Start count value
'''
def makeSingleEven(arr, start):
​
    # compute the limit row/colums of each of 4 odd magic squares
    sz = len(arr)
    szDv2 = sz // 2
    lims = [
        (0, szDv2-1, 0, szDv2-1),
        (szDv2, sz-1, szDv2, sz-1),
        (0, szDv2-1, szDv2, sz-1),
        (szDv2, sz-1, 0, szDv2-1)
        ]
    strt = start
​
    # Compute the four magic squares
    for lms in lims:
        ar, strt = makeOdd(arr, lms, strt)
​
    size = len(arr)
​
    # Swap 1st left regions of 4 magic square block.
    delRw = size // 2
    ra1, ra2 = 0, (size // 4) - 1
    rb1, rb2 = ra1 + delRw, ra2 + delRw
    c1, c2 = 0, (size // 4) - 1
    tmp = [[2 for i in range(size)] for j in range(size)]
    swapArrays(arr, ra1, ra2, rb1, rb2, c1, c2)
​
    # Swap 2nd left regions of 4 magic square block.
    delRw = ra2 - ra1
    ra1 = ra2 + 2
    ra2 = ra1 + delRw
    rb1 = rb2 + 2
    rb2 = rb1 + delRw
    swapArrays(arr, ra1, ra2, rb1, rb2, c1, c2)
​
    # Swap 3rd left regions of 4 magic square block.
    ra1-= 1;
    ra2 = ra1
    rb1 -= 1
    rb2 = rb1
    c1 += 1
    c2 += 1
    swapArrays(arr, ra1, ra2, rb1, rb2, c1, c2)
​
    # Swap right regions of 4 magic square block.
    if(size > 6):
        ra1, ra2 = 0, (size // 2) - 1
        rb1, rb2 = size // 2, size - 1
        c2 = size - 1
        c1 = c2 - ((size // 4) - 2)
        swapArrays(arr, ra1, ra2, rb1, rb2, c1, c2)
    return arr, 0
​
#--------------------------------------------------------------
'''
Check if row/column in r/c bounds defined by regions
    regions - regions to check
    r,c - row/column
'''
def inRegions(regions, r, c):
    for r1, r2, c1, c2 in regions:
        if((r >= r1) and (r <= r2) and (c >= c1) and (c <= c2)):
            return True
    return False
​
#--------------------------------------------------------------
'''
Make even magic square divisable by 4
    arr - 2d array initialized to -1
'''
def makeDoubleEven(arr):
    size = len(arr)
    regions = []
​
    szSm = (size // 4)
    szLg = (size // 2)
​
    # Compute top center region
    r1 = 0
    r2 = r1 + szSm - 1
    c1 = szSm
    c2 = c1 + szLg - 1
    regions.append([r1, r2, c1, c2])
​
    # Compute bottom center region
    r1 += (szSm + szLg)
    r2 += (szSm + szLg)
    regions.append([r1, r2, c1, c2])
​
    # Compute mid left region
    r1 = szSm
    r2 = r1 + szLg -1
    c1 = 0
    c2 = c1 + szSm - 1
​
    # Compute mid right region
    regions.append([r1, r2, c1, c2])
    c1 += (szSm + szLg)
    c2 += (szSm + szLg)
    regions.append([r1, r2, c1, c2])
​
    lst = []
​
    # First pass - fill in numbers inside regions
    cnt = 1
    for r in range(len(arr)):
        for c in range(len(arr)):
            if(inRegions(regions, r, c)):
               arr[r][c] = cnt
            else:
               lst.insert(0, cnt)
            cnt += 1
​
    # Second pass - fill in remaining numbers outside regions
    for r in range(len(arr)):
        for c in range(len(arr)):
            if(not inRegions(regions, r, c)):
               arr[r][c] = lst.pop(0)
​
    return arr, 0
​
#--------------------------------------------------------------
def make_magic(size):
    sum = (size * ((size ** 2) + 1)) / 2
    sm1 = size - 1
    arr = [[-1 for i in range(size)] for j in range(size)]
​
    # Make odd magic square
    if((size % 2) == 1):
        lims = (0, sm1, 0, sm1)
        v, c = makeOdd(arr, lims, 1)
        return v
​
    # Make even magic square not divisable by 4
    elif((size % 4) != 0):
        v, c = makeSingleEven(arr, 1)
        return v
​
    # Make even magic square divisable by 4
    else:
        v, c = makeDoubleEven(arr)
        return v

