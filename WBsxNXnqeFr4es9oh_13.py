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
​
def clockwise_cipher(message):
    width = math.ceil(math.sqrt(len(message)))
    table = [[None for _ in range(width)] for _ in range(width)]
    msg = message + ' ' * (width**2 - len(message))
    
    w = width
    width -= 1
    index = 0
    b = 0
    while width > 0:
        for i in range(width):
            table[b][b+i] = msg[index]
            table[b+i][w-1-b] = msg[index + 1]
            table[w-1-b][w-1-b-i] = msg[index + 2]
            table[w-1-b-i][b] = msg[index + 3]
            index += 4
        b += 1
        width -= 2
    if width == 0:
        center = math.floor(w/2)
        table[center][center] = msg[-1]
        
    result = ''
    for row in table:
        for val in row:
            result += val
    return result

