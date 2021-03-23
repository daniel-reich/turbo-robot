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

import math
def clockwise_cipher(message):
    gs = math.ceil(len(message) ** 0.5)
    order = math.ceil(gs / 2)
    grid = [[' '] * gs for _ in range(gs)]
    coords = []
    output = ''
    for j in range(order):
        gsb = gs - (j * 2)
        for i in range(gsb - 1):
            p1 = [j, i + j]
            p2 = [i + j, gsb - 1 + j]
            p3 = [gsb - 1 + j, gsb - 1 - i + j]
            p4 = [gsb - 1 - i + j, j]
            coords += p1, p2, p3, p4
    if gs ** 2 == len(message):
        coords += [[order - 1, order - 1]]
​
    for i in range(len(message)):
        c1 = coords[i][0]
        c2 = coords[i][1]
        grid[c1][c2] = message[i]
​
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            output += grid[i][j]
    return output

