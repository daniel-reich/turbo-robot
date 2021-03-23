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

def clockwise_cipher(message):
    size = 1
    while size**2 < len(message):
        size += 1
    grid = [[' ' for _ in range(size)] for __ in range(size)]
    cur_size = size
    offset = 0
    idx = 0
    while idx < len(message) and cur_size > 1:
        for k in range(cur_size-1):
            grid[offset][offset+k] = message[idx]
            idx += 1
            if idx >= len(message): break
            if k < cur_size - 1:
                grid[offset+k][size-1-offset] = message[idx]
                idx += 1
                if idx >= len(message): break
            grid[size-1-offset][size-1-offset-k] = message[idx]
            idx += 1
            if idx >= len(message): break
            if k < cur_size - 1:
                grid[size-1-offset-k][offset] = message[idx]
                idx += 1
                if idx >= len(message): break
        offset += 1
        cur_size -= 2
    if len(message) == size**2:
        grid[size//2][size//2] = message[-1]
    ans = ""
    for row in grid:
        #print(''.join(row))
        ans += ''.join(row)
    return ans

