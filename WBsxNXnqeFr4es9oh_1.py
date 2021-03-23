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

from math import ceil
def make_cycle(s, n):
    side, res = [s + i * 4 for i in range(n - 1)], []
    for _ in range(4):
        res.append(side)
        side = [x + 1 for x in side]
    return res
​
def make_square(size):
    res, s = [[0] * size for _ in range(size)], 1
    for i in range(size // 2):
        len_edge = size - i * 2
        lst_nums = make_cycle(s, len_edge)
        for idx, v in enumerate(lst_nums[0]):
            res[i][i + idx] = v
        for idx, v in enumerate(lst_nums[1]):
            res[i + idx][i + len_edge - 1] = v
        for idx, v in enumerate(lst_nums[2]):
            res[i + len_edge - 1][i + len_edge - 1 - idx] = v
        for idx, v in enumerate(lst_nums[3]):
            res[i + len_edge - 1 - idx][i] = v
        s += (len_edge - 1) * 4
    if size % 2:
        center = (size - 1) // 2
        res[center][center] = size * size
    return res
​
def clockwise_cipher(msg):
    len_msg = len(msg)
    square_size = ceil(pow(len_msg, 0.5))
    msg = " {}{}".format(msg, (square_size * square_size - len_msg) * " ")
    idx_square = make_square(square_size)
    res = [[msg[col] for col in row] for row in idx_square]
    return "".join("".join(row) for row in res)

