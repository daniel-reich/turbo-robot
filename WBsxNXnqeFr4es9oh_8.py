"""


In **Clockwise Cipher** , encoding is done by placing message characters in
the corner cells of a square and moving in a clockwise direction.

Create a function that takes an argument `message`, and returns the **encoded
message**.

There are some variations on the rules of encipherment. One version of the
cipher rules are outlined below:

    message = "Mubashir Hassan"
    
    clockwise_cipher(message) ➞ "Ms ussahr nHaaib"

 **Step 1:** Form a square large enough to fit all the message characters.
Given message can fit in a 4 x 4 square.

 **Step 2:** Starting with the top-left corner, place message characters in
the corner cells moving in a clockwise direction. After the first cycle is
complete, continue placing characters in the cells following the last one in
its respective row/column. When the outer cells are filled, continue for the
remaining inner squares:

M| s| | u  
---|---|---|---  
s| s| a| h  
r| | n| H  
a| a| i| b  
  
 **Step 3:** Return encoded message **Rows-wise** :

    eMessage = "Ms ussahr nHaaib"

### Example for a 5 x 5 Square

    [ 1  5  9 13  2]
    [16 17 21 18  6]
    [12 24 25 22 10]
    [ 8 20 23 19 14]
    [ 4 15 11  7  3]

### Examples

    clockwise_cipher("Mubashir Hassan") ➞ "Ms ussahr nHaaib"
    
    clockwise_cipher("Matt MacPherson") ➞ "M ParsoMc nhteat"
    
    clockwise_cipher("Edabit is amazing") ➞ "Eisadng  tm    i   zbia a"

### Notes

  * Fill up any unused cells with a space character.
  * Message can contain spaces and special characters.

"""

def clockwise_cipher(txt):
    '''
    Returns txt scrambled via the clockwise square cipher as per instructions.
    '''
    from math import ceil
​
    size = len(txt)
    d = ceil(size**0.5)   # dimension of the square
    grid = [[' ' for _ in range(d)] for _ in range(d)]  # space fill grid
    place(txt, grid, size, d)
​
    return ''.join(grid[i][j] for i in range(d) for j in range(d))
​
def place(txt, grid, size, d):
    '''
    Places the characters in txt into grid as per the clockwise square algorithm
    '''
    m = d // 2  # the midpoint of the grid
    p = 0
    for i in range(m):
        for j in range(i, d-i-1):
            for r, c in ((i,j),(j,d-i-1),(d-i-1,d-j-1),(d-j-1,i)):
                grid[r][c] = txt[p]
                p += 1
                if p == size:
                    return  # finished populating grid
    grid[m][m] = txt[-1]   # d is odd and size = d^2

